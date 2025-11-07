import re

import wmi
import uuid
import winreg

class DetectVM:
    def __init__(self):
        try:
            self.c = wmi.WMI()
        except Exception :
            print(f"[ERROR] Cannot connect to WMI: {e}")
            exit(1)

    def check_system_info(self):
        system_info = self.c.Win32_ComputerSystem()[0]
        bios_info = self.c.Win32_BIOS()[0]

        manufacturer = system_info.Manufacturer.lower()
        model = system_info.Model.lower()
        bios = bios_info.SMBIOSBIOSVersion.lower()

        vm_keywords = ['vmware', 'virtualbox', 'qemu', 'kvm']
        all_info = manufacturer + " " + model + " " + bios

        if any(keyword in all_info for keyword in vm_keywords):
            return True
        else:
            return False
    
    def check_mac(self):
        mac = uuid.getnode()
        mac_prefix = ':'.join(['{:02x}'.format((mac >> ele) & 0xff) for ele in range(40, -1, -8)])[:8]
        vm_mac_prefixes = ["00:05:69", "00:0C:29", "00:1C:14", "00:50:56", "52:54:00", "00:15:5D"]

        return any(mac_prefix.upper().startswith(p.upper()) for p in vm_mac_prefixes)
    
    def check_disk(self):
        try:
            for disk in self.c.Win32_DiskDrive():
                model = getattr(disk, 'Model', '') or ''
                manuf = getattr(disk, 'Manufacturer', '') or ''
                combined = f"{model} {manuf}"
                for pat in [r'VMware', r'VIRTUAL', r'QEMU', r'KVM', r'QEMU HARDDISK']:
                    if re.search(pat, combined, re.IGNORECASE):
                        return True
        except Exception as e:
            print(f"[WARN] WMI disk query failed: {e}")
        return False
    
    def detect_vm(self):
        score = 0
        if self.check_system_info():
            score += 4
        elif self.check_mac():
            score += 3
        elif self.check_disk():
            score += 3

        if score >= 5:
            return True
         
        return False
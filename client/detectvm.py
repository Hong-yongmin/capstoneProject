import wmi
from cpuid import cpuid
import uuid
import winreg

class DetectVM:
    def check_system_info(self):
        c = wmi.WMI()
        system_info = c.Win32_ComputerSystem()[0]
        bios_info = c.Win32_BIOS()[0]

        manufacturer = system_info.Manufacturer.lower()
        model = system_info.Model.lower()
        bios = bios_info.SMBIOSBIOSVersion.lower()

        vm_keywords = ['vmware', 'virtualbox', 'qemu', 'kvm']
        all_info = manufacturer + " " + model + " " + bios

        if any(keyword in all_info for keyword in vm_keywords):
            return True
        else:
            return False
        
    def check_cpuid(self):
        eax, ebx, ecx, edx = cpuid(1)
        return bool(ecx & (1 << 31))
    
    def check_mac(self):
        mac = uuid.getnode()
        mac_prefix = ':'.join(['{:02x}'.format((mac >> ele) & 0xff) for ele in range(40, -1, -8)])[:8]
        vm_mac_prefixes = ["00:05:69", "00:0C:29", "00:1C:14", "08:00:27", "52:54:00", "00:15:5D"]

        return any(mac_prefix.upper().startswith(p.upper()) for p in vm_mac_prefixes)
    
    def check_registry(self):
        try:
            with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"HARDWARE\DESCRIPTION\System") as key:
                bios_version, _ = winreg.QueryValueEx(key, "SystemBiosVersion")
                bios_version = ' '.join(bios_version).lower()
                if any(v in bios_version for v in ['virtualbox', 'vmware', 'qemu', 'xen', 'hyper-v']):
                    return True
        except Exception:
            pass
        return False
    
    def detect_vm(self):
        score = 0
        if self.check_system_info():
            score += 1
        elif self.check_cpuid():
            score += 1
        elif self.check_mac():
            score += 1
        elif self.check_registry():
            score += 1

        if score >= 2:
            return True
         
        return False
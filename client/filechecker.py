class FileChecker:
    def __init__(self):
        self.extension = ['txt', 'pdf', 'hwp', 'jpeg', 'jpg', 'png']
        self.magic = [b'\x25\x50\x44\x46\x2D\x31\x2E\x34', #pdf
                      b'\xD0\xCF\x11\xE0\xA1\xB1\x1A\xE1', #hwp
                      b'\x89\x50\x4E\x47\x0D\x0A\x1A\x0A', #png
                      b'\xFF\xD8\xFF\xE1\x79\xFE\x45\x78'] #jpg
        
    def check_extension(self, file_extension):
        if file_extension.lower() in self.extension:
            return True
        else:
            return False
        
    def check_magic(self, file_byte):
        if file_byte in self.magic:
            return True
        else:
            return False
        
    def check_file(self, file):
        file_extension = file.split('.')[-1]
        if self.check_extension(file_extension):
            return True
        
        with open(file, 'rb') as f:
            file_byte = f.read(8)
            if self.check_magic(file_byte):
                return True
            
        return False
    
    def check_encrypted_file(self, file):
        file_extension = file.split('.')[-1]
        if file_extension == 'encrypted':
            return True
        
        return False
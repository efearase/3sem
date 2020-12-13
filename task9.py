import os

os.system('df -Th /')

disk = os.statvfs('/')
print('Availible size:',(disk.f_bavail * disk.f_frsize) / 1024)
print('Free size:', (disk.f_bfree * disk.f_frsize) / 1024)

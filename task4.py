import sys
import os
import stat

if len(sys.argv) != 3:
    print('Usage: %s some-file' % sys.argv[0])
    sys.exit(1)

name_from = sys.argv[1]
name_to = sys.argv[2]

if not os.path.exists(name_from):
    print('Ошибка файла')
    sys.exit(2)

current_permissionsfrom = stat.S_IMODE(os.lstat(name_from).st_mode)
current_permissionsto= stat.S_IMODE(os.lstat(name_to).st_mode)

os.chmod(name_to, 0o000)
os.chmod(name_to, current_permissionsto or current_permissionsfrom)

stinfo = os.stat(name_from)
os.utimes(name_to, (stinfo.st_atime, stinfo.st_mtime))

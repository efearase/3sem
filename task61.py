import os
import sys
from stat import *

if len(sys.argv) != 2:
    print('Usage: %s some-file' % sys.argv[0])
    sys.exit(1)

path = sys.argv[1]

mode = os.stat(path).st_mode
if not S_ISDIR(mode):
    print('Введенный файл не является директорией')
    sys.exit(2)

for dirs,folder,files in os.walk(path):
    print('Selected folder: ', dirs)
    print('Subfolders ', folder)
    for entry in files:
        mode_entry = os.stat(entry).st_mode
        if S_ISREG(mode_entry):
            print('%s located at this folder is a reg file' % entry)
        elif S_ISBLK(mode_entry):
            print('%s is a block special device file' % entry)
        elif S_ISLNK(mode_entry):
            print('%s located at this folder is a a symbolic link' % entry)
        else:
            print('%s located at this folder is something else' % entry)

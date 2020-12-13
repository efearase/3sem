import os, sys
from stat import *

if len(sys.argv) != 2:
    print('Usage: %s some-file' % sys.argv[0])
    sys.exit(1)

path = sys.argv[1]

mode = os.stat(path).st_mode
if S_ISDIR(mode):
    print('It is a directory')
elif S_ISREG(mode):
    print('It is a reg file')
elif S_ISBLK(mode):
    print('It is a block special device file')
elif S_ISLNK(mode):
    print('It is a a symbolic link')
else:
    print('It is something else')

print('Size of file is:', os.stat(path).st_size  )
print('Number of hard links is:', os.stat(path).st_nlink  )
print('Time of most recent content modification expressed in seconds:',os.stat(path).st_mtime)
print(os.stat(path))


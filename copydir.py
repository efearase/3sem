import os
import shutil
import sys

if len(sys.argv) != 3:
    print('Usage: %s some-file' % sys.argv[0])
    sys.exit(1)

root_src_dir = sys.argv[1]
root_dst_dir = sys.argv[2]

for src_dir, dirs, files in os.walk(root_src_dir):
    dst_dir = src_dir.replace(root_src_dir, root_dst_dir, 1)
    if not os.path.exists(dst_dir):
        os.makedirs(dst_dir)
    for file_ in files:
        src_file = os.path.join(src_dir, file_)
        dst_file = os.path.join(dst_dir, file_)
        if os.path.exists(dst_file):
            os.remove(dst_file)
        shutil.copy(src_file, dst_dir)
        size = os.path.getsize(src_file)
        current = 0
        if not os.path.exists(dst_file):
            with open(src_file, 'rb') as src:
                with open(dst_file, 'wb') as dst:
                    while (size - current > 4096):
                        to_.write(src.read(4096))
                        current += 4096
                        src.seek(current)
                    dst.write(src.read(size - current))
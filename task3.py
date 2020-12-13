import sys
import os

if len(sys.argv) != 3:
    print('Usage: %s some-file' % sys.argv[0])
    sys.exit(1)

name_from = sys.argv[1]
name_to = sys.argv[2]

if not os.path.isfile(name_from):
    print('Ошибка файла')
    sys.exit(2)

current = 0
size = os.path.getsize(name_from)

if not os.path.exists(name_to):
    with open(name_from, 'rb') as from_:
        with open(name_to, 'wb') as to_:
            while (size - current > 4096) :
                to_.write(from_.read(4096))
                current += 4096
                from_.seek(current)
            to_.write(from_.read(size - current))

elif not os.path.isfile(name_to):
    print('Ошибка файла')
    sys.exit(3)

else:
    with open(name_from, 'rb') as from_:
        with open(name_to, 'wb') as to_:
            while (size - current > 4096):
                to_.write(from_.read(4096))
                current += 4096
                from_.seek(current)
            to_.write(from_.read(size - current))
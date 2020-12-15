import os
import sys

if len(sys.argv) != 3:
    print('Неверное количество аргументов')
    sys.exit(1)

path = sys.argv[1]
text = sys.argv[2]

elif not os.path.isfile(path):
    print('Ошибка файла')
    sys.exit(2)

written_len = 0
len_to_write = len(text)
seek = 0
with open(path, 'rb') as f:
    while (len_to_write - written_len > 4096):
        f.write(text[seek:seek+4096])
        written_len += 4096
    to_.write(text[seek: len(text-1)])

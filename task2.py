import os
import sys

if len(sys.argv) != 3:
    print('Неверное количество аргументов')
    sys.exit(-2)

path = sys.argv[1]
text = sys.argv[2]

with open(path,'wb') as file:
    file.write(text.encode('utf-8'))

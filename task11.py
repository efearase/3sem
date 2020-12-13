import fcntl, os, time
counter_file = 'counter.txt'
if not os.path.exists(counter_file):
    counter_file = open('counter.txt', 'w')
    counter_file.write('0')
    counter_file.close()
counter_file = open('counter.txt', 'r+')
fcntl.flock(counter_file.fileno(), fcntl.LOCK_EX)
count = int(counter_file.readline()) + 1
counter_file.seek(0)
counter_file.write(str(count))
counter_file.close()
while(True):
    a = 1
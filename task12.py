import os

pid = os.fork()
if pid != 0:
    os.waitpid(pid, 0)

print(pid)
import os
import psutil
import json
import sys

pid = os.fork()
if pid != 0:
    os.waitpid(pid, 0)

if pid == 0:
    print("Child pid:", pid)
    print ("Current working dir for child : %s" % os.getcwd())
    print("Supplementary group IDs associated with the child process:")
    print(os.getgroups() )
else:
    print("Current working dir for parent : %s" % os.getcwd())
    print("Supplementary group IDs associated with the parent process:")
    print(os.getgroups())
    print("Parent pid:", pid)
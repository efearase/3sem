import os
import pwd
import grp
import time

def print_info(pid):
    print("Process Id:", pid)

    uid = os.getuid()
    print("Real user ID of the current process:", uid)

    struct_pwd = pwd.getpwuid(uid)

    gid = struct_pwd[3]

    print("Login name:", struct_pwd[0])
    print("Numerical group ID", gid)
    print("User home directory", struct_pwd[5])
    print("User command interpreter", struct_pwd[6])

    struct_grd = grp.getgrgid(gid)

    print("The name of the group", struct_grd[0])
    print("All the group member’s user names", struct_grd[3])

    print("Current working dir for process : %s" % os.getcwd())
    print("Supplementary group IDs associated with the process process:")
    print(os.getgroups())






pid = os.fork()

if pid != 0:
    time.sleep(1)
else:
    ppid = os.getppid()
    while os.getppid() == ppid:
        a='a'
    print_info(pid)
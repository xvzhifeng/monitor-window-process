import os

import psutil


def get_info():
    for proc in psutil.process_iter():
        print(proc.name())
        if proc.name() == "test.exe":
            print("hello test")

def get_info_name(name):
    for proc in psutil.process_iter():
        print(proc.name())
        if proc.name() == name:
            return True
    return False

def get_count_process(name):
    count = 0
    for proc in psutil.process_iter():
        print(proc.name())
        if proc.name() == name:
            count+=1
    print(count)
    return count

def find_process_name(name):
    command = '"tasklist | findstr  \"{0}\""'.format(name)
    # 如果存在则返回 0 ，不存在返回 1
    info  = os.system(command)
    print(info)
    return info == 0


def kill_process_name(name):
    command = '"taskkill /F /IM {0}"'.format(name)
    print(command)
    os.system(command)

if __name__ == "__main__":
    # get_info()
    find_process_name("Code.exe")
    # kill_process_name
    get_count_process("Code.exe")
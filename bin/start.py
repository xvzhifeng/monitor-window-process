import time
import lib.process_operarot as process
import lib.bat_operator as bat

def start(args):
    while True:
        print("check result is : ".format(process.get_count_process(args[1]) != int(args[2])))
        if process.get_count_process(args[1]) != int(args[2]):
            process.kill_process_name(args[1])
            bat.bat_start(args[3])
            print("restart success")
        time.sleep(int(args[4]))
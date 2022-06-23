import time
import lib.process_operarot as process
import lib.bat_operator as bat

def start(args):
    while True:
        if process.get_count_process(args[1]) != args[2]:
            process.kill_process_name(args[1])
            bat.bat_start(args[3])
            print("重启成功")
        time.sleep(1000)
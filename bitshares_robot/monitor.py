import os
import platform
import time
import psutil

base_path = "/home/foxfei/PycharmProjects/bitshares_robot/safe_src/trunk/bitshares_robot/"
log_stat = os.stat(path + "log/logging.log")

if log_stat.st_mtime + 300 < time.time():
    for proc in psutil.process_iter():
        if proc.name() == 'start_uc_fool.s':
            proc.terminate()
    os.system(path + 'nohup sh start_uc_fool.sh &')

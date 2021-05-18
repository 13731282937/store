



import threading
import time

class PCManger(threading.Thread):

    def run(self) -> None:
        for i in range(100):
            time.sleep(0.5)
            print("电脑管家正在杀毒，已经扫描",i, "个病毒")

class Manger360(threading.Thread):

    def run(self) -> None:
        for i in range(100):
            time.sleep(0.5)
            print("360正在杀毒，已经扫描",i ,"个病毒")

m360 = Manger360()
mpc = PCManger()

m360.start()
mpc.start()
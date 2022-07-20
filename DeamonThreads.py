from threading import *
import time
def display():
    for i in range(10):
        time.sleep(1)
        print('Child thread')
t = Thread(target = display)
t.setDaemon(True)
t.start()
time.sleep(7)
print('Main thread execution')
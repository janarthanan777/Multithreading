from threading import *
import time
def display():
    print('It is a child thread, named with daemon charac: ', current_thread().daemon)
    t2 = Thread(target = display2)
    t2.start()
def display2():
    print('This child has inherited the daemon properties from its parent, proof:',current_thread().daemon)

t1 = Thread(target = display)
t1.name = 'JP'
t1.setDaemon(True)
t1.start()
t1.join()
print("This is the main thread, proof", current_thread().name)
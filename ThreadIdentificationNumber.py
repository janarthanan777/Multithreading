from threading import *
def display():
    print('Child thread', current_thread().ident)
t = Thread(target = display)
t.start()
t.join()
print('Main thread identification number :', current_thread().ident)
print('Child thread identification number:', t.ident)

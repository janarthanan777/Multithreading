from threading import *
def display():
    for i in range(1):
        print('The code is executed by:', current_thread().name)
t = Thread(target= display) # do not use display(), do not declare the function just give its name, bas.
t.name = 'jannu'
t.start()
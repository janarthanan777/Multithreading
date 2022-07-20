from threading import *
class Test:
    def display(self):
        for i in range(10):
            print('Child Thread')
t = Test()
obj = Thread(target=t.display)
obj.start()
for i in range(10):
    print('Main thread ')
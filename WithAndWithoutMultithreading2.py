import time
from threading import *
def doubles(numbers):
    for n in numbers:
        time.sleep(1)
        print('Double:', 2 * n)
def sqaures(numbers):
    for n in numbers:
        time.sleep(1)
        print('Sqaure:', n*n)
numbers = [1, 2, 3, 4, 5, 6]
begintime = time.time()
t1 = Thread(target=sqaures, args=(numbers, ))
t2 = Thread(target=doubles, args=(numbers, ))
t1.start()
t2.start()
t1.join()
t2.join()
endtime = time.time()
print('Total time taken = ', endtime - begintime)
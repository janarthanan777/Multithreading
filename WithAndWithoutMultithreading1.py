import time
def doubles(numbers):
    for n in numbers:
        time.sleep(1)
        print('DOuble:', 2 * n)
def sqaures(numbers):
    for n in numbers:
        time.sleep(1)
        print('Sqaure:', n*n)
numbers = [1, 2, 3, 4, 5, 6]
begintime = time.time()
doubles(numbers)
sqaures(numbers)
endtime = time.time()
print('Total time taken = ', endtime - begintime)
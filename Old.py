import random
import time
N = 1000
A = []
for n in range(N):
    A = random.sample(range(-N*10, N*10), N)

def old(A):
    dmin = 1000000000
    for i in range(len(A)):
        for j in range(len(A)):
            if i != j and abs(A[i] - A[j]) < dmin:
                dmin = abs(A[i] - A[j])
    return dmin


def new(A):
    dmin = 1000000000
    for i in range(len(A)-1):
        for j in range(i+1, len(A)):
            d = abs(A[i] - A[j])
            if d < dmin:
                dmin = d

    return dmin

start = time.time()
print(new(A), time.time() - start)
start = time.time()
print(old(A), time.time() - start)

import random
import time
A = random.sample(range(1, 10000000), 1000000)

def bad_sort(A):
    S = [0]*len(A)
    Count = [0]*len(A)
    for i in range(len(A)):
        Count[i] = 0
    for i in range(len(A)-1):
        for j in range(i+1,len(A)):
            if A[i] < A[j]:
                Count[j] += 1
            else:
                Count[i] += 1
    for i in range(len(A)):
        S[Count[i]] = A[i]
    return S

start = time.time()
print(bad_sort(A), time.time() - start)
start = time.time()
A.sort()
print(A, time.time() - start)

import random

def insert(heap, value):
    heap.append(value)
    upheap(heap)

def upheap(heap):
    index = len(heap)-1
    while heap[index//2] > heap[index]:
        heap[index//2], heap[index] = heap[index], heap[index//2]
        index = index//2

def remove(heap):
    heap[0], heap[len(heap)-1] = heap[len(heap)-1], heap[0]
    value = heap.pop()
    if len(heap) > 1:
        downheap(heap)
    return value

def downheap(heap):
    index = 0
    prev = -1
    while prev != index:
        prev = index
        if 2*prev < len(heap) and heap[2*prev] < heap[index]:
            index = 2*prev
        if 2*prev+1 < len(heap) and heap[2*prev+1] < heap[index]:
            index = 2*prev+1
        heap[prev], heap[index] = heap[index], heap[prev]



numbers = random.sample(range(0,10000), 10000)
heap = [0]

for x in numbers:
    insert(heap, x)
for i in range(len(heap)):
    print(remove(heap))

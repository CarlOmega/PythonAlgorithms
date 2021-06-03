import random
import time

class SelectionSort:
    def __init__(self, numbers):
        self.numbers = []
        for x in numbers:
            self.numbers.append(x)

    def sort(self):
        for i in range(len(self.numbers)):
            min = i
            for j in range(i, len(self.numbers)):
                if self.numbers[j] < self.numbers[min]:
                    min = j
            self.numbers[i], self.numbers[min] = self.numbers[min], self.numbers[i]
        return self.numbers

class InsertionSort:
    def __init__(self, numbers):
        self.numbers = []
        for x in numbers:
            self.numbers.append(x)

    def sort(self):
        for i in range(1, len(self.numbers)):
            for j in range(i, 0, -1):
                if self.numbers[j] < self.numbers[j-1]:
                    self.numbers[j-1], self.numbers[j] = self.numbers[j], self.numbers[j-1]
                else:
                    break
        return self.numbers

class BubbleSort:
    def __init__(self, numbers):
        self.numbers = []
        for x in numbers:
            self.numbers.append(x)

    def sort(self):
        for i in range(0, len(self.numbers)-1):
            for j in range(0, len(self.numbers)-1-i):
                if self.numbers[j+1] < self.numbers[j]:
                    self.numbers[j+1], self.numbers[j] = self.numbers[j], self.numbers[j+1]
        return self.numbers

class MergeSort:
    def __init__(self, numbers):
        self.numbers = []
        for x in numbers:
            self.numbers.append(x)

    def sort(self):
        return self.mergeSort(self.numbers)

    def mergeSort(self, A):
        if len(A) == 1:
            return A

        mid = len(A)//2
        left = self.mergeSort(A[:mid])
        right = self.mergeSort(A[mid:])
        return self.merge(left, right)

    def merge(self, left, right):
        merged = []
        a = 0
        b = 0
        while a < len(left) and b < len(right):
            if left[a] <= right[b]:
                merged.append(left[a])
                a += 1
            else:
                merged.append(right[b])
                b += 1
        if a < len(left):
            merged = merged + left[a:]
        if b < len(right):
            merged = merged + right[b:]
        return merged

class QuickSort:
    def __init__(self, numbers):
        self.numbers = []
        for x in numbers:
            self.numbers.append(x)

    def sort(self):
        self.quicksort(0, len(self.numbers)-1)
        return self.numbers

    def partition(self, low, high):
        pivot = low
        for i in range(low+1, high+1):
            if self.numbers[i] <= self.numbers[low]:
                pivot += 1
                self.numbers[i], self.numbers[pivot] = self.numbers[pivot], self.numbers[i]
        self.numbers[pivot], self.numbers[low] = self.numbers[low], self.numbers[pivot]
        return pivot

    def quicksort(self, low, high):
        if low >= high:
            return
        pivot = self.partition(low, high)
        self.quicksort(low, pivot-1)
        self.quicksort(pivot+1, high)

class HeapSort:
    def __init__(self, numbers):
        self.heap = [0]
        for x in numbers:
            self.insert(x)

    def sort(self):
        sorted = []
        for _ in range(len(self.heap)-1):
            sorted.append(self.remove())
        return sorted

    def insert(self, value):
        self.heap.append(value)
        self.upheap()

    def upheap(self):
        index = len(self.heap)-1
        while self.heap[index//2] > self.heap[index]:
            self.heap[index//2], self.heap[index] = self.heap[index], self.heap[index//2]
            index = index//2

    def remove(self):
        if len(self.heap) <= 1:
            return False
        self.heap[0], self.heap[len(self.heap)-1] = self.heap[len(self.heap)-1], self.heap[0]
        value = self.heap.pop()
        if len(self.heap) > 1:
            self.downheap()
        return value

    def downheap(self):
        index = 0
        prev = -1
        while prev != index:
            prev = index
            if 2*prev < len(self.heap) and self.heap[2*prev] < self.heap[index]:
                index = 2*prev
            if 2*prev+1 < len(self.heap) and self.heap[2*prev+1] < self.heap[index]:
                index = 2*prev+1
            self.heap[prev], self.heap[index] = self.heap[index], self.heap[prev]

class RadixSort:
    def __init__(self, numbers):
        self.numbers = []
        for x in numbers:
            self.numbers.append(x)

    def sort(self):
        buckets = [[] for x in range(10)]
        for i in range(1, 7):
            digit = 10**i
            for x in self.numbers:
                d = (x%digit)//10**(i-1)
                buckets[d].append(x)
            self.numbers = []
            for b in buckets:
                self.numbers += b
            buckets = [[] for x in range(10)]
        return self.numbers

numbers = random.sample(range(0,1000000), 100000)
#
# selection = SelectionSort(numbers)
# start = time.time()
# selection.sort()
# print("Sort: {0:10} Time {1:.2f}".format("Selection", time.time() - start))
#
# insertion = InsertionSort(numbers)
# start = time.time()
# insertion.sort()
# print("Sort: {0:10} Time {1:.2f}".format("Insertion", time.time() - start))
#
# bubble = BubbleSort(numbers)
# start = time.time()
# bubble.sort()
# print("Sort: {0:10} Time {1:.2f}".format("Bubble", time.time() - start))

merge = MergeSort(numbers)
start = time.time()
merge.sort()
print("Sort: {0:10} Time {1:.2f}".format("Merge", time.time() - start))

quick = QuickSort(numbers)
start = time.time()
quick.sort()
print("Sort: {0:10} Time {1:.2f}".format("Quick", time.time() - start))

heap = HeapSort(numbers)
start = time.time()
heap.sort()
print("Sort: {0:10} Time {1:.2f}".format("Heap", time.time() - start))

radix = RadixSort(numbers)
start = time.time()
radix.sort()
print("Sort: {0:10} Time {1:.2f}".format("Radix", time.time() - start))

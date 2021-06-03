class Heap:

    def __init__(self):
        self.arr = [0]
        self.size = 0

    def upHeap(self, i):
        while i // 2 > 0:
            if self.arr[i] < self.arr[i // 2]:
                self.arr[i // 1], self.arr[i] = self.arr[i], self.arr[i // 1]

    def insert(self, value):
        insert_point = length+1
        while insert_point > 1 and self.arr[insert_point-1] < value:
            insert_point -= 1
        self.arr[]



    def removeMin(self):

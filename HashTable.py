

class ClosedHashTable:
    def __init__(self, size):
        self.table = [None]*size
        self.size = size
        self.count = 0

    def hash_function(self, value):
        return value%self.size

    def insert(self, value):
        key = self.hash_function(value)
        if self.count < self.size:
            while self.table[key] != None:
                key = (key+1)%self.size
            self.table[key] = value
            self.count += 1
            return True
        else:
            return False

    def remove(self, value):
        key = self.hash_function(value)
        while self.table[key] != None:
            if self.table[key] == value:
                self.table[key] = None
                self.count -= 1
                key = (key+1)%self.size
                while self.table[key] != None:
                    temp = self.table[key]
                    self.table[key] = None
                    self.count -= 1
                    self.insert(temp)
                    key = (key+1)%self.size
                return value
            key = (key+1)%self.size
        return False

    def check(self, value):
        key = self.hash_function(value)
        while self.table[key] != None:
            if self.table[key] == value:
                return True
            key = (key+1)%self.size
        return False

    def __str__(self):
        return "[" + ", ".join(["({0}, {1:4})".format(i, str(self.table[i])) for i in range(len(self.table))]) + "]"

stuff = [1, 4, 4, 5, 6, 7, 9, 10, 12, 14, 16, 17, 19, 20]
hash_table = ClosedHashTable(len(stuff))
for i in stuff:
    hash_table.insert(i)
    print(hash_table)
print("__________________________________________________")
for i in stuff:
    hash_table.remove(i)
    print(hash_table)

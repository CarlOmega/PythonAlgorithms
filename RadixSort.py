import random
numbers = [random.randint(0,1000000) for x in range(1000000)]

def radix_sort(numbers):
    buckets = [[] for x in range(10)]
    for i in range(1, 7):
        digit = 10**i
        for x in numbers:
            d = (x%digit)//10**(i-1)
            buckets[d].append(x)
        numbers = []
        for b in buckets:
            numbers += b
        buckets = [[] for x in range(10)]
    return numbers

print(numbers)
print(radix_sort(numbers))

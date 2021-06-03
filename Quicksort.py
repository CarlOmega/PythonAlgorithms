import random

def partition(array, low, high):
    pivot = low
    for i in range(low+1, high+1):
        if array[i] <= array[low]:
            pivot += 1
            array[i], array[pivot] = array[pivot], array[i]
    array[pivot], array[low] = array[low], array[pivot]
    return pivot

def quicksort(nums, low, high):
    if low >= high:
        return
    pivot = partition(nums, low, high)
    quicksort(nums, low, pivot-1)
    quicksort(nums, pivot+1, high)

nums = [random.randint(0,10) for x in range(10)]
print(nums)
quicksort(nums, 0, len(nums)-1)
print(nums)

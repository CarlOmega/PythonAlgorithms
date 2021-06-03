import random

def partition(nums, low, high):
    pivot = low
    for i in range(low+1, high+1):
        if nums[i] <= nums[low]:
            pivot += 1
            nums[i], nums[pivot] = nums[pivot], nums[i]
    nums[pivot], nums[low] = nums[low], nums[pivot]
    return pivot

def quicksort(nums, low, high):
    if low >= high:
        return
    p = partition(nums, low, high)
    quicksort(nums, low, p-1)
    quicksort(nums, p+1, high)

nums = [random.randint(0,10) for x in range(10)]
print(nums)
quicksort(nums, 0, len(nums)-1)
print(nums)

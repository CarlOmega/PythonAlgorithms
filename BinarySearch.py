searching_stuff = [1, 4, 4, 5, 6, 7, 9, 10, 12, 14, 16, 17, 19, 20]

def recursive_search(A, l, h, x):
    if l > h:
        return -1
    m = (l+h)//2
    if A[m] > x:
        return recursive_search(A, l, m-1, x)
    elif A[m] < x:
        return recursive_search(A, m+1, h, x)
    else:
        return m


def interitive_search(A, l, h, x):
    while (l <= h):
        m = (l+h)//2
        if A[m] > x:
            h = m-1
        elif A[m] < x:
            l = m+1
        else:
            return m
    return -1

search_number = 11
print(recursive_search(searching_stuff, 0, len(searching_stuff)-1, search_number))
print(interitive_search(searching_stuff, 0, len(searching_stuff)-1, search_number))

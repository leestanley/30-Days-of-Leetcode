# Complete the findNumber function below.
def findNumber(arr, k):
    if k in arr:
        return 'YES'
    else:
        return 'NO'


# Complete the oddNumbers function below.
def oddNumbers(l, r):
    arr = []
    for i in range(l,r+1):
        if i % 2 == 1:
            arr.append(i)
    return arr

# Best runtime
# Heap Sort

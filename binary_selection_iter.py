"""
Sort a given array using the binary selection algorithm.
"""

def binarySelectionIter(n, arr):
    start = 0
    stop  = len(arr) - 1
    while start <= stop: 
        mid = (start + stop) // 2
        if n == arr[mid]:
            return f'{n} found at index: {mid}'
        elif n > arr[mid]:
            start = mid + 1
        else: 
            stop = mid - 1
    return f'{n} not found in list.'

def createList(max_val):
    arr = []
    [arr.append(num) for num in range(1, max_val+1)]
    return arr

l =  createList(50)


# for num in l:
#     print(binarySelectionIter(num, l))

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#  [ 0  1  2  3  4  5  6  7  8  9 ]
# initial middle of l is 4, or value of 5
print(binarySelectionIter(7, l))
from mergesort import merge_sorted

def divide_arr(arr):
    if len(arr) < 2:
        print(f'Base condition reached with {arr[:]}')
        return arr[:]
    else:
        middle = len(arr)//2
        print('Current list to work with:', arr)
        print('Left split:', arr[:middle])
        print('Right slit: ', arr[middle:])
        l1 = divide_arr(arr[:middle])
        l2 = divide_arr(arr[middle:])
        return(merge_sorted(l1, l2))

l = [6, 8, 1, 4, 10, 7, 8, 9, 3, 2, 5]
divide_arr(l)
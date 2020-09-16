def biSection_Recur(n, arr, start, stop):
    if start > stop: 
        return f'{n} not found in list!'
    else: 
        mid = (start + stop) // 2
        if n == arr[mid]:
            return f'{n} found at index: {mid}'
        elif n > arr[mid]:
            return biSection_Recur(n, arr, mid+1, stop)
        else:
            return biSection_Recur(n, arr, start, mid-1)

def create_list(max_val):
    arr = []
    [arr.append(num) for num in range(1, max_val+1)]
    return arr

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#idx 0  1  2  3  4  5  6  7  8  9

for num in range(16):
    print(biSection_Recur(num, l, 0, len(l)-1))
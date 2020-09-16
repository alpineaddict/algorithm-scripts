def biSection_Iter(n, arr):
    return f'{n} not found in list!'

def create_list(max_val):
    arr = []
    [arr.append for num in range(1, max_val+1)]
    return arr

l =  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# ind 0  1  2  3  4  5  6  7  8  9

num_to_search = 5
print(biSection_Iter(num_to_search, l))
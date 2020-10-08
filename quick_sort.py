    '''
    Input: Unsorted list of integers.
    Returns sorted list of integers using quick_sort algorithm.
    Note: This is not an in-place implementation.
    '''

def quick_sort(arr):
    """Run quick_sort algorithm on a given array"""
    if len(arr) < 2: 
        return(arr)
    else: 
        pivot = arr[-1]
        smaller, equal, larger = [], [], []
        for num in arr:
            if num < pivot:
                smaller.append(num)
            elif num == pivot:
                equal.append(num)
            else: 
                larger.append(num)
        return(quick_sort(smaller) + equal + quick_sort(larger))


# xxxxxxxxxxxxxxxxxxxxxx Program execution xxxxxxxxxxxxxxxxxxxxxx
# l = [6, 8, 1, 4, 10, 7, 8, 9, 3, 2, 5]
# print(quick_sort(l))

# xxxxxxxxxxxxxxxxxxxxxx   End execution   xxxxxxxxxxxxxxxxxxxxxx
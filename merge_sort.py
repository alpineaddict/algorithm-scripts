# Steps
# 1. Compare first element in each list and append smaller element
# 2. Using a indices and iterator, perform same comparison for all
#    elements in both lists
# 3. Move marker up by 1 position after smaller number is found
# 4. Copy remaining list once comparisons are complete and there 
#    are items still remaining in one of the lists

def merge_Sorted(arr1,arr2):
    # print("Merge function called with lists below:")
    # print(f"left: {arr1} and right: {arr2}")
    sorted_arr = []
    i, j = 0, 0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            sorted_arr.append(arr1[i])
            i += 1
        else: 
            sorted_arr.append(arr2[j])
            j += 1
        #print(sorted_arr)
    while i < len(arr1):
        sorted_arr.append(arr1[i])
        i += 1
    while j < len(arr2):
        sorted_arr.append(arr2[j])
        j += 1

    return(sorted_arr)


def merge_Sort(arr):
    if len(arr) < 2:
        # print(f'Base condition reached with {arr[:]}')
        return arr[:]
    else:
        middle = len(arr)//2
        # print('Current list to work with:', arr)
        # print('Left split:', arr[:middle])
        # print('Right slit: ', arr[middle:])
        l1 = merge_Sort(arr[:middle])
        l2 = merge_Sort(arr[middle:])
        return(merge_Sorted(l1, l2))



# xxxxxxxxxxxxxxxxxxxxxx Program execution xxxxxxxxxxxxxxxxxxxxxx
# l = [6, 8, 1, 4, 10, 7, 8, 9, 3, 2, 5]
# print(merge_Sort(l))

# xxxxxxxxxxxxxxxxxxxxxx   End execution   xxxxxxxxxxxxxxxxxxxxxx


# Originally used for merge sort before merge_Sort implementation
# l1 = [2,4,6,8,10]
# l2 = [1,3,5,7,8,9]
# print(f'Merged list: {merge_Sorted(l1,l2)}')



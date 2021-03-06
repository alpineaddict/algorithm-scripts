"""
Various sorting algorithms listed below to use in conjunction with
performance analyzer script to measure run time of different algorithms
"""

def quick_sort(array):
    """ Accept an array of unsorted integers and return array of sorted
    integers via quick_sort algorithm. """
    if len(array) < 2: 
        return(array)
    else: 
        pivot = array[-1]
        smaller, equal, larger = [], [], []
        for num in array:
            if num < pivot:
                smaller.append(num)
            elif num == pivot:
                equal.append(num)
            else: 
                larger.append(num)
        return quick_sort(smaller) + equal + quick_sort(larger)

def merge_sorted(arr1,arr2):
    """ Accept 2 arrays of unsorted integers and return array of sorted
    integers via merge_sort algorithm. """
    sorted_arr = []
    i, j = 0, 0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            sorted_arr.append(arr1[i])
            i += 1
        else: 
            sorted_arr.append(arr2[j])
            j += 1
    while i < len(arr1):
        sorted_arr.append(arr1[i])
        i += 1
    while j < len(arr2):
        sorted_arr.append(arr2[j])
        j += 1

    return sorted_arr

def merge_sort(array):
    """ Perform merge_sort algorithm on array of unsorted integers. """
    if len(array) < 2:
        return array[:]
    else:
        middle = len(array)//2
        l1 = merge_sort(array[:middle])
        l2 = merge_sort(array[middle:])
        return merge_sorted(l1, l2)

def bubble_sort(array):
    """ Perform bubble_sort algorithm on array of unsorted integers. """
    swap_happened = True
    while swap_happened:
        swap_happened = False
        for num in range(len(array) - 1):
            if array[num] > array[num+1]:
                swap_happened = True
                array[num], array[num+1] = array[num+1], array[num]

def selection_sort(array):
    """ Perform selection_sort algorithm on array of unsorted integers. """
    counter = 0
    while counter < len(array):
        for num in range(counter, len(array)):
            if array[num] < array[counter]:
                array[counter], array[num] = array[num], array[counter]
        counter += 1            
    
    return array
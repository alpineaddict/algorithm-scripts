#!/usr/bin/env python

"""
Sort an array using the bubble sort algorithm. 
"""

def bubble_Sort(arr):
    swap_happened = True

    while swap_happened:
        # print('Bubble sort status: ' + str(arr))
        swap_happened = False
        for num in range(len(arr) - 1):
            if arr[num] > arr[num+1]:
                swap_happened = True
                arr[num], arr[num+1] = arr[num+1], arr[num]
        return(arr)

# xxxxxxxxxxxxxxxxxxxxxx Program execution xxxxxxxxxxxxxxxxxxxxxx
# l = [6,8,1,4,10,7,8,9,3,2,5]
# bubble_Sort(l)

# xxxxxxxxxxxxxxxxxxxxxx   End execution   xxxxxxxxxxxxxxxxxxxxxx
#!/usr/bin/env python

# Insert Sort Algorithm
# Run through list of n elements ONE time and dynamically perform sorting while
# moving through list and checking at each iteration of the list that the 
# current number is greater than the previous number.

def insertion_sort(arr):
    '''
    Accept array containing n elements as parameter and perform numerical sort 
    on array. Sequential iteration through entire list should only happen once.
    In other words, the outer most for loop should only need to run once in 
    order to sort the entire array.
    '''

    key = 1
    # [6,1,8,4,10]
    
    print(f'Initial array to sort: {arr}')
    for elem in range(len(arr)):
        # check if number before key is less than key. if so, perform swap, then
        # move backwards through list
        try:
            if arr[key] < arr[key-1]:
                wrk_index = key
                arr[key],arr[key-1] = arr[key-1],arr[key]   
                # after a swap, work backwords through list to beginning
                for item in range(len(arr[:key])):
                    try:
                        if arr[wrk_index] < arr[wrk_index -1]:
                            arr[wrk_index],arr[wrk_index-1] \
                            = arr[wrk_index-1],arr[wrk_index]
                        wrk_index -= 1
                    except:
                        pass
            key += 1            
        except:
            pass
    print(f'Completed  array sort: {arr}')


arr = [6,1,8,4,10]
insertion_sort(arr)    

arr2 = [72, 8, 6, 1, 32, 40, 13]
insertion_sort(arr2)

arr3 = [16,11,81,14,110]
insertion_sort(arr3)
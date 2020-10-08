#!/usr/bin/env python

"""
Script built to test and report performance of various sorting algorithms.
Sorting algorithms covered in sorting_algorithms module.
Take input from user (size of list, max value of range, iterations) and 
run each sorting algorithm with input paramaters and report performance in 
seconds.
"""

from time import time
from random import randint
from sorting_algorithms import *
import sys; sys.setrecursionlimit(1000000)

def get_user_input():
    '''
    Get input from user for the size of the array (number of items), the
    desired max value of any number within the array, and lastly the number
    of iterations to run each algorithm.
    '''
    size_of_list = int(input('What size list do you want to create? '))
    max_number  = int(input('What is the max value of the range? '))
    iterations = int(input('How many iterations do you want to run? '))

    return size_of_list, max_number, iterations

def build_array(size_of_list, max_number):
    '''
    Generate list of random values based off of user input and run algorithms
    with said input. Return array. 
    '''
    arr = []
    [arr.append(randint(1, max_number)) for num in range(1, size_of_list+1)]

    return arr

def analyze_func(func_name, arr):
    '''
    Take in function name and array as parameters. Measure time in seconds
    to run function and print the output. 
    '''
    
    start = time()
    func_name(arr)
    stop  = time()
    seconds = stop - start
    print(f'{func_name.__name__.capitalize()}\t -> Elapsed time: {seconds:.5f}')


if __name__ == '__main__':
    counter = 1
    print('Algorithms file loaded.')
    print('-'*40)
    size_of_list, max_number, iterations = get_user_input()
    arr = build_array(size_of_list, max_number)

    for num in range(iterations):   
        print(f'Run: {num +1}')
        arrCopy = arr.copy()
        analyze_func(quickSort, arr)
        analyze_func(bubbleSort, arrCopy)
        analyze_func(mergeSort, arr)
        analyze_func(selectionSort, arr)
        analyze_func(sorted, arr)
        print('-'*40)
    print('Finished! Terminating program.')

    # for num in range(5):
    #     analyze_func(quick_Sort, arr)

#!/usr/bin/env python

# performanceAnalyzer.py

# Script built to test and report performance of various sorting algorithms. 
# Take input from user (size of list, max value of range, iterations) and 
# run different algorithms with input paramaters and report performance in 
# seconds. 

from time import time
from random import randint
from sortingAlgorithms import *
import sys; sys.setrecursionlimit(1000000)

# Get input from user
def get_User_Input():
    '''
    Get input from user for the size of the array (number of items), the
    desired max value of any number within the array, and lastly the number
    of iterations to run each algorithm.
    '''
    sizeOfList = int(input('What size list do you want to create? '))
    maxNumber  = int(input('What is the max value of the range? '))
    iterations = int(input('How many iterations do you want to run? '))

    return(sizeOfList, maxNumber, iterations)

def build_Array(sizeOfList, maxNumber):
    '''
    Generate list of values based off of user input and run algorithms with
    said input. Return array. 
    '''
    
    # Generate list of random numbers
    arr = []
    [arr.append(randint(1, maxNumber)) for num in range(1, sizeOfList+1)]

    return(arr)    


def analyze_Func(funcName, arr):
    '''
    Take in function name and array as parameters. Measure time in seconds
    to run function and print the output. 
    '''
    
    start = time()
    funcName(arr)
    stop  = time()
    seconds = stop - start
    print(f'{funcName.__name__.capitalize()}\t -> Elapsed time: {seconds:.5f}')


  ##########################
 ### Program execution #### 
##########################
counter = 1
print('Algorithms file loaded.')
print('-'*40)
sizeOfList, maxNumber, iterations = get_User_Input()
arr = build_Array(sizeOfList, maxNumber)

# Loop through # of requested times
for num in range(iterations):   
    print(f'Run: {num +1}')
    arrCopy = arr.copy()
    analyze_Func(quick_Sort, arr)
    analyze_Func(bubble_Sort, arrCopy)
    analyze_Func(merge_Sort, arr)
    analyze_Func(selection_Sort, arr)
    analyze_Func(sorted, arr)
    # build_Analyzer(build_Array, sizeOfList, maxNumber)
    print('-'*40)
print('Finished! Terminating program.')

# for num in range(5):
#     analyze_Func(quick_Sort, arr)



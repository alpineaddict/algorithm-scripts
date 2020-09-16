#!/usr/bin/env python

# BinarySelection_EmailSearch will prompt a user for a number of email addresses
# to generate and for one email address to search for. The script will then run
# a binary selection algorithm on the list and search for the email address that
# was specified by the user. The script will use the runtime analyzer function
# to record and report the performance time to complete both operations

# Script Outline
# User prompt for # of emails to generate as well as email address to search for
# Run binary select recursive function to find the email
# Use runtime analyzer to report back performance results for finding email


import string, random
from time import time
from random import randint

# Algorithm & performance analyzer
def binary_Section_Email_Search(emailToSearch, nameList):
    start = 0
    stop  = len(nameList) - 1
    while start <= stop: 
        mid = (start + stop) // 2    
        if emailToSearch == nameList[mid]:
            return f'{emailToSearch} found at index: {mid}'
        elif emailToSearch > nameList[mid]:
            start = mid + 1
        else: 
            stop = mid - 1
    return f'{emailToSearch} not found in list.'

def binary_Section_Email_Search_Recursion(emailToSearch, nameList, start, stop):
    if start > stop: 
        return f'{emailToSearch} not found in list!'
    else: 
        mid = (start + stop) // 2
        if emailToSearch == nameList[mid]:
            return f'{emailToSearch} found at index: {mid}'
        elif emailToSearch > nameList[mid]:
            return binary_Section_Email_Search_Recursion(
                emailToSearch, nameList, mid+1, stop)
        else:
            return binary_Section_Email_Search_Recursion(
                emailToSearch, nameList, start, mid-1)

def analyze_Func(funcName, arr, *args):
    '''
    Take in function name and array as parameters. Measure time in seconds
    to run function and print the output. 
    '''
    
    if 'generate' in funcName.__name__.lower():
        start = time()
        funcName(arr, *args)
        stop  = time()
        seconds = stop - start
        print(f'{funcName.__name__.capitalize()}\t\t -> \
            Elapsed time: {seconds:.5f}')
    else: 
        start = time()
        print(funcName(arr, *args))
        stop  = time()
        seconds = stop - start
        print(f'{funcName.__name__.capitalize()}\t\t -> \
            Elapsed time: {seconds:.5f}')

# Email generation functions
# Get input from user for number of emails to generate and address to search for
def get_User_Input():
    numberOfEmails = int(input('How many email addresses would you like to ' +
                        'generate? '))
    emailToSearch  = input('Please an email address to search for: ')
    return numberOfEmails, emailToSearch

# Generate list of email addresses, add search email to list
def generate_List_Of_Emails(numberOfEmails, emailToSearch):
    '''
    Domains for email addresses: [@example.com, @example.org, @example.info]
    '''
    nameList = []
    alphabet = string.ascii_lowercase
    domainList = ['@example.com', '@example.org', '@example.info']

    # Create list totalling the value of numberOfEmails
    while len(nameList) < numberOfEmails:
        name = ''
        for num in range(12):
            name += alphabet[randint(0, len(alphabet)-1)]
        emailAddr = name + domainList[randint(0, len(domainList)-1)]
        nameList.append(emailAddr)

    # Append email to search onto the list, then sort entire list
    nameList.append(emailToSearch)
    nameList = sorted(nameList)

    # return sorted list
    return nameList


  #####################
 # Program execution #
#####################
numberOfEmails, emailToSearch = get_User_Input()
nameList = generate_List_Of_Emails(numberOfEmails, emailToSearch)

analyze_Func(binary_Section_Email_Search, emailToSearch, nameList)
analyze_Func(binary_Section_Email_Search_Recursion, emailToSearch, nameList, 0,
            len(nameList) -1)
analyze_Func(generate_List_Of_Emails, numberOfEmails, emailToSearch)

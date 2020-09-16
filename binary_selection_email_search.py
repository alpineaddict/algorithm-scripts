#!/usr/bin/env python

"""
BinarySelection_EmailSearch will prompt a user for a number of email addresses
to generate and for one email address to search for. The script will then run
a binary selection algorithm on the list and search for the email address that
was specified by the user. The script will use the runtime analyzer function
to record and report the performance time to complete both operations

Script Outline
User prompt for # of emails to generate as well as email address to search for.
Run binary select recursive function to find the email.
Use runtime analyzer to report back performance results for finding email.
"""

import string, random
from time import time
from random import randint

# Algorithm & performance analyzer
def binarySectionEmailSearch(email_to_search, name_list):
    """Accept email to search for as well as list of names"""
    start = 0
    stop  = len(name_list) - 1
    while start <= stop: 
        mid = (start + stop) // 2
        if email_to_search == name_list[mid]:
            return f'{email_to_search} found at index: {mid}'
        elif email_to_search > name_list[mid]:
            start = mid + 1
        else: 
            stop = mid - 1
    return f'{email_to_search} not found in list.'

def binarySectionEmailSearchRecursion(email_to_search, name_list, start, stop):
    """
    Accept email to search for as well as list of names in addition to a 
    start and stop point to utilize recursion.
    """
    if start > stop: 
        return f'{email_to_search} not found in list!'
    else: 
        mid = (start + stop) // 2
        if email_to_search == name_list[mid]:
            return f'{email_to_search} found at index: {mid}'
        elif email_to_search > name_list[mid]:
            return binarySectionEmailSearchRecursion(
                email_to_search, name_list, mid+1, stop)
        else:
            return binarySectionEmailSearchRecursion(
                email_to_search, name_list, start, mid-1)

def analyzeFunc(func_name, arr, *args):
    '''
    Take in function name and array as parameters. Measure time in seconds
    to run function and print the output. 
    '''
    
    if 'generate' in func_name.__name__.lower():
        start = time()
        func_name(arr, *args)
        stop  = time()
        seconds = stop - start
        print(f'{func_name.__name__.capitalize()}\t\t -> \
            Elapsed time: {seconds:.5f}')
    else:
        start = time()
        print(func_name(arr, *args))
        stop  = time()
        seconds = stop - start
        print(f'{func_name.__name__.capitalize()}\t\t -> \
            Elapsed time: {seconds:.5f}')

# Email generation functions
def getUserInput():
    """
    Get user input for number of emails to generate & address to search for
    """
    number_of_emails = int(input('How many email addresses would you like to ' +
                        'generate? '))
    email_to_search  = input('Please an email address to search for: ')
    return number_of_emails, email_to_search

# Generate list of email addresses, add search email to list
def generateListOfEmails(number_of_emails, email_to_search):
    """Generate list of emails based off of user input"""
    '''
    Domains for email addresses: [@example.com, @example.org, @example.info]
    '''
    name_list = []
    alphabet = string.ascii_lowercase
    domain_list = ['@example.com', '@example.org', '@example.info']

    while len(name_list) < number_of_emails:
        name = ''
        for num in range(12):
            name += alphabet[randint(0, len(alphabet)-1)]
        email_addr = name + domain_list[randint(0, len(domain_list)-1)]
        name_list.append(email_addr)

    name_list.append(email_to_search)
    name_list = sorted(name_list)

    return name_list


if __name__ == '__main__':
    number_of_emails, email_to_search = getUserInput()
    name_list = generateListOfEmails(number_of_emails, email_to_search)
    analyzeFunc(binarySectionEmailSearch, email_to_search, name_list)
    analyzeFunc(binarySectionEmailSearchRecursion, email_to_search, name_list, 0,
                len(name_list) -1)
    analyzeFunc(generateListOfEmails, number_of_emails, email_to_search)


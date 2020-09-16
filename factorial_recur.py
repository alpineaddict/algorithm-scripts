""" Perform factorial algorithm on a number in recrusion fashion """

def factorial_recur(n):
    if n == 0:
        return(1)
    else:
        return(n*factorial_recur(n-1))

z = 0 # Expecting 1
print(f'The value of {z}! is {factorial_recur(z)}')

z = 1 # Expecting 1
print(f'The value of {z}! is {factorial_recur(z)}')

z = 5 # Expecting 120
print(f'The value of {z}! is {factorial_recur(z)}')
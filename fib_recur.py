""" Simple fibonacci sequence algorithm """

def fibRecur(n):
    if n == 0:
        return(0)
    elif n == 1:
        return(1)        
    else: 
        return(fibRecur(n-1) + fibRecur(n-2))

def fibRunner(z):
    print(f'The {z}th number in the fibonacci sequence is {fibRecur(z)}')

z = 0
fibRunner(z)

z = 1
fibRunner(z)

z = 10
fibRunner(z)

#6) Write a Python function to calculate the factorial of a number (a non-negati#ve integer). The function acc
#epts the number as an argument.


def factorial(n):

    fact=1
    i=1
    while i<=n:
        fact=fact*i 
        i = i + 1  
    print(fact) 
        
factorial(5)
factorial(4)



#7) Using for loop, write and run a Python program to find factorial from 0 to
# 10.



def factorial(n):

    fact=1
    i=1
    while i<=n:
        fact=fact*i 
        i = i + 1  
        print(fact) 
        
factorial(10)

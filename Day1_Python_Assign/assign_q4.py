

#4] Write a Python function to find the maximum of three numbers.

num1= int(input("Enter value for num1 : "))
num2= int(input("Enter value for num2 : "))
num3= int(input("Enter value for num3 : "))
if (num1>=num2) and (num1>=num3):
    print("num1 is maximum")

else:
    if(num2>=num1) and (num2>=num3):
       print("num2 is maximum")
    else:
        print("num3 is maximum")

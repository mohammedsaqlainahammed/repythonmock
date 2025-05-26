# factorial number means product of all positive integers
# less than or equal to a given positive integer.
num= int(input("enter a number:"))
fact = 1
if num<0:
    print("factorial does not exist for negative number")
elif num==0:
    print("the factorial of 0 is 1")
else:
    for i in range(1,num+1):
        fact=fact*i
        print("the factorial of",num,"is",fact)

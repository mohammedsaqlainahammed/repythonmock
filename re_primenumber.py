# prime number means number divisible by one and itself.

num = int(input("enter a number:"))
for i in range(2,num):
    if num%i==0:
        print(num,"is not a prime number")
        break
    else:
        print(num,"is a prime number")
        break
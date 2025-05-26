# a sequence of numbers where each number is the sum of the two preceding
# numbers,typically starting with 0&1
def fib(num):
   a=0
   b=1
   if num<=0:
       print("please enter a positive integer.")
   elif num == 1:
       print(a)
   else:
       print(a)
       print(b)
       for i in range(2,num):
           c=a+b
           print(c)
           a=b
           b=c

    #call the function here

fib(6)


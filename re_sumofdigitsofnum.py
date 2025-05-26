# adding each individual digit of that number together.
num = int(input("enter a number : "))
Sum = 0 #ex 234
while num>0: # 234>0
    rem=num%10  #rem=234%10=4
    Sum = Sum+rem #sum=0+4=4
    num = num // 10  # num= 234//10=23
    print(Sum)
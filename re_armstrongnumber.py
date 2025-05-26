# armstrong number means: sum of cubes of individual digit = given number.
number=int(input("enter a number here: "))
length = len(str(number))
temp = number
Sum = 0
while temp > 0:
    digit = temp % 10
    Sum += digit ** length
    temp = temp // 10

    print("number is {} and sum is {}".format(number,Sum))

    if Sum==number:
        print("it is an armstrong number")
    else:
        print("it is not an armstrong number")

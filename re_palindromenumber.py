# palindrome: a number that is unchanged or same after reversed.
num=(input("enter a number:"))
if num == num[::-1]:
    print(f"{num} is palindrome")
else:
    print(f"{num} is not a palindrome")
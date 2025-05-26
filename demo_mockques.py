from dataclasses import replace

print("HELLO".lower())

print("  hello  ".strip())

print("banana".replace("b","B"))

#f- strings help format strings easily using variables inside{}
name = "alice"
age = 25
print(f"my name is {name} and i am {age} years old")


# reverse string using a function
def reverse_string(s):
    return s[::-1]
print(reverse_string("apple"))
#Write a python  porgram to swap 2 numbers without using a third variable

a = int(input("Enter the first number : "))
b = int(input("Enter the second number : "))

a = a+b
b = a-b
a = a-b

print("Value after swapping is ",a)
print("Value after swapping is ",b)
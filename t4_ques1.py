#   Write a program to take two inputs a and b,swap their values using a temporary variable and print updated values

a = int(input("Enter the first number : "))
b = int(input("Enter the second number : "))

c = a 
a  = b 
b = c

print("Value after swapping is ",a)
print("Value after swapping is ",b)
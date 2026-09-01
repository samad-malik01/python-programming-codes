# Write a python program to take age as input and print True if age is between18 and 60 otherwise print false

age = int(input("Enter the age :"))
if age < 18:
    print("False")
elif age <60:
    print("True")
else:
    print("False")
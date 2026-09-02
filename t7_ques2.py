#write a python program to take student name and roll number, then generate a username using the first 3 letters of the name and the last two digits of the roll number
name = input("Enter student name: ")
roll_number = input("Enter roll number: ")
user_name = name[0:3]+roll_number[-2:]
print(user_name)
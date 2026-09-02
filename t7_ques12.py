#write a python program to take password and check whether it contains @ and has at least 8 characters
password = input("Enter a password: ")
print("@" in password and len(password)>=8)
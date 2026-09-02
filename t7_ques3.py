#write a python program to take a email address and print the domain name
email = input("Enter email: ")
domain = email[email.find("@") + 1:]
print("Domain Name: ",domain )
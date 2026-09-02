#take an email address and check whether it contains @ and .com
email = input("Enter an email address: ")
new = "@" in email and ".com" in email
print(new)
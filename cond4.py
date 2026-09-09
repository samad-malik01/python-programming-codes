'''write a python program to create a simple password validation system.
The program shoukd repeatedly ask the user to enter a password until a valid password is entered.
A password will be considered valid only if it has atleast 8 characters and contains the @ symbol.
Once the user enters a valid password, the program shoukd display "Password accepted." and stop.
Otherwise , it should display display "Weak Password.Try again." and ask for the password again.'''

password = input("Enter password: ")
while len(password) < 8 or "@" not in password:
    print("Weak password.Try again.")
    password = input("Enter password: ")

print("Password accepted.")
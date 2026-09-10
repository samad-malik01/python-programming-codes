 #write a python aprogram that asks the user to enter a username and password. The user shoukd get omly 3 attempts. If the correct credentials are entered, display"Login SuccesSfull" and stop the loop. If all attempts are used, display"Account Locked".

correct_username = "admin"
correct_password = "abc@123"
for i in range(0,3):
    uname = input("Enter a username: ")
    password = input("Enter a password: ") 
    if uname == correct_username and password == correct_password:
        print("Login Successfull.")
        break
    else:
        print("Account Locked.")

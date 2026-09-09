#write a python program to stimulate a digital lock system.
#the lock should ask the user to enter a 4-digit pin if the entered pin does not contain exactly 4 digits, the program should display an error message and ask again. if the the entered pin is correct, the lock should open otherwise the program should ask the user to try again.

correct_pin = "1234"
while True:
    pin = input("Enter a 4-digit PIN: ")
    if len(pin) != 4:
        print("Please enter exactly 4 digits")
    elif pin == correct_pin:
        print("Lock Opened!")
        break
    else:
         print("Wrong PIN. Try Again.")
#write a python program to take a digit 10-digit mobile number and display only the last 4 digits. Replace the first 6 digits with ******
mobile =input("Enter mobile number: ")
masked="******"+mobile[-4:]
print("Masked mobile number =", masked)
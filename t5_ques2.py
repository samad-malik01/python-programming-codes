# Write a python prorgam to take marks of three sub out of 100. Print True if s=the student atleast 40 in all three subjects and average marks are at least 50

m1 = int(input("Marks of 1st sub :"))
m2 = int(input("Marks of 2nd sub :"))
m3 = int(input("Marks of 3rd sub :"))

avg = (m1+m2+m3)//3

if m1 > 40 and m2 >40 and m3>40 and avg>50:
    print("True")
else:
    print("False")

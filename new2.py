''' write a python pogram to input a number and check whether it is prime or not.'''
num = int(input("Enter a number: "))
if num>1:
    for i in range(2,num):
        num%i == 0
        print("Number is not prime")
        break
    else:
        print("Number is prime")

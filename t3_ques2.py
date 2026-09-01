#write a python program to take 2 digits as input and print the sum of digits

n =int(input())   # 2 digit
num = n//10
rem = n%10
print(f"sum of digits of  is : {num + rem}")

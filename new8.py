'''write a python program to repeatedly calculate the sum of a number until the result becomes a single digit.Example: 9875 -> 9+8+7+5 = 29 -> 2+9 = 11 -> 1+1 = 2'''

n = int(input("Enter a number: "))
sum = 0
while n > 9:
    while n > 0:
        sum = sum + n % 10
        n = n // 10
    n = sum
    sum = 0
    print(n)
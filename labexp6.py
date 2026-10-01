'''Write a program to reverse every kth row in a matrix.'''
r = int(input("Enter number of rows: "))
c = int(input("Enter number f columns: "))
matrix =[]
for i in range(r):
    row = list(map(int, input().split()))
    matrix.append(row)
k = int(input("Enter k: "))
for i in range(k - 1, r, k):
    matrix[i].reverse()
print("Matrix after reversing every kth row")
for row in matrix:
    print(*row)
# print an inverted right angled triangle

print("Inverted Right angled triangle")
n=5
for i in range(n):
    for i in range(i,n):
        print("*",end =" ")
    for j in range(i+1):
        print(" ",end ="")
    print()
    

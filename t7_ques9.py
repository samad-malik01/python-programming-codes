#write a python program to take a word and print it in reverse order using slicing. Also check whether it is the same forward and backward
word = input("Enter a word: ")
res =word[::-1]
print(res)
if word == res:
    print("Yes")
else:
    print("No")
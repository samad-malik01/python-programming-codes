#write a python program to take a string and separate characters present at even index positions and odd index positions
string = input("Enter a string: ")
even = string[0::2]
odd = string[1::2]
print("Character at even index: ", even)
print("Character at odd index: ", odd)
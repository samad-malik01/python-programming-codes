# Write a python program to take a student's full name and display:
# """
# .Total numbers of character
# .First character
# .Last character
# .Name in uppercase
# """

name = input("Enter Full Name: ")
print("Total number of characters:",len(name))
print("First character: ",name[0])
print("Last characterf: ",name[-1])
print("Name in Uppercase: ",name.upper())

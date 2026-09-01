 # Write a python program to fill the given letter template with name and date.

letter = """""
Dear <Name>,
You are selected!
<Date>
"""

Date = (input("Enter the date :"))
name = input("Enter your name :")

letter =letter.replace("<Name>", name)
letter =letter.replace("<Date", Date)
print(letter)
# res = f"Dear {name},\nYou are selected!\n{Date}"
# print(res)
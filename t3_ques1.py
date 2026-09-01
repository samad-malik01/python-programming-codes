#Write a python program to take total minutes as input and convert into hours and remaining minutes

min = int(input())
hours = min//60
rem_min=min % 60
print(f"Reamining hours are {hours} and minutes is {rem_min}")



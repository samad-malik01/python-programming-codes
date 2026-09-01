#Write a python program to takw an amount in rupees and calculate how many notes of rs 500 and 100 are needed 

n =int(input("Enter the amount : "))

print(f"Number of 500 notes req are {n//500}")
a = n%500
print(f"Number of 100 notes req are {a//100}")
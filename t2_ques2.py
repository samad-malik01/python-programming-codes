# write a python program to calculate simple interest and total amount using Principal ,Rate and time entered by the user

p = int(input())
rate = int(input())
time = int(input())
SI = ( p*rate*time) / 100
print(SI)

total_amount = (p+SI)
print(total_amount)

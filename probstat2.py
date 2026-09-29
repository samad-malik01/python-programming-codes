'''Practice Problems

2. Write a Python program to allocate seats to a group in a single row of a cinema hall. First, input the total number of seats n. Then enter the status of each seat:

1. 0 means the seat is available.
2. 1 means the seat is already booked.

Next, input the number of people in the group. The program must find the first consecutive block of available seats that can accommodate the entire group. If such seats are found:

1. Book all those seats by changing their status from 0 to 1.
2. Display the allocated seat numbers as a tuple.
3. Display the updated list of seat statuses.

If no consecutive block is available, display "Consecutive seats not available" and print the original seat list without any changes.

Conditions:
1. Seat numbering starts from 1.
2. The group size must be at least 1 and cannot exceed n.
3. All group members must be allotted seats together in consecutive order.
4. If more than one suitable block is available, allocate the first block from the left.
5. Input seat status must be either 0 or 1.

Example:
Enter number of seats: 9
Seat status: [1, 0, 0, 1, 0, 0, 0, 0, 1]
Enter group size: 3

Expected Output:
Allocated seats: (5, 6, 7)
Updated seats: [1, 0, 0, 1, 1, 1, 1, 0, 1]'''

n = int(input("Enter number of seats: "))

seats = []

for i in range(n):
    x = int(input("Enter seat status (0/1): "))
    seats.append(x)

group = int(input("Enter group size: "))

found = False

for i in range(n - group + 1):

    count = 0

    for j in range(group):
        if seats[i + j] == 0:
            count = count + 1

    if count == group:

        allocated = []

        for j in range(group):
            seats[i + j] = 1
            allocated.append(i + j + 1)

        print("Allocated seats:", tuple(allocated))
        print("Updated seats:", seats)

        found = True
        break

if found == False:
    print("Consecutive seats not available")
    print("Seats:", seats)
import sys

class Lab:
    def __init__(self, capacity):
        self.capacity = capacity
        self.bookings = {}          # group -> seats

    def free_seats(self):
        return self.capacity - sum(self.bookings.values())

    def book(self, group, seats):
        if group in self.bookings or seats > self.free_seats():
            return False
        self.bookings[group] = seats
        return True

    def cancel(self, group):
        if group not in self.bookings:
            return False
        del self.bookings[group]
        return True

def main():
    data = sys.stdin.read().split()
    labs = {"A": Lab(int(data[0])), "B": Lab(int(data[1]))}
    n = int(data[2])
    pos = 3
    rejected = 0

    for _ in range(n):
        op = data[pos]
        if op == "BOOK":
            lab, group, seats = data[pos + 1], data[pos + 2], int(data[pos + 3])
            pos += 4
            if not labs[lab].book(group, seats):
                rejected += 1
        else:  # CANCEL
            lab, group = data[pos + 1], data[pos + 2]
            pos += 3
            if not labs[lab].cancel(group):
                rejected += 1

    print(labs["A"].free_seats(), labs["B"].free_seats())
    print(rejected)

main()
'''Create a BankAccount class that stores an account holder’s name and balance. Add instance methods to deposit money, withdraw money, and display the balance. Do not allow a withdrawal greater than the available balance.'''
class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount
    def display(self):
        print("Account Holder:", self.name)
        print("Balance:", self.balance)
name = input("Enter account holder name: ")
balance = float(input("Enter initial balance: "))
b1 = BankAccount(name, balance)
deposit = float(input("Enter deposit amount: "))
b1.deposit(deposit)
withdraw = float(input("Enter withdrawal amount: "))
b1.withdraw(withdraw)
b1.display()
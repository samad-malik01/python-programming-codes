'''Create a Product class with the product name, price, and quantity. Add an instance method to calculate the total cost. Take these values from the user and display the product name and total cost.'''
class Product:
    def __init__(self,name,price,quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    def total_cost(self):
        return self.price * self.quantity
name = input("Enter product name: ")
price = float(input("Enter price: "))
quantity = int(input("Enter quantity: "))
p1 = Product(name,price,quantity)
print("Product Name: ", p1.name)
print("Total cost: ", p1.total_cost())
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

class Shopkeeper:
    def __init__(self):
        self.inventory = []

    def add_product(self, name, price, quantity):
        product = Product(name, price, quantity)
        self.inventory.append(product)
        print(f'Product {name} added to inventory.')

    def view_inventory(self):
        if not self.inventory:
            print("Inventory is empty.")
            return
        for product in self.inventory:
            print(f'Name: {product.name}, Price: {product.price}, Quantity: {product.quantity}')

    def record_sale(self, name, quantity):
        for product in self.inventory:
            if product.name == name:
                if product.quantity >= quantity:
                    product.quantity -= quantity
                    print(f'Sold {quantity} units of {name}.')
                else:
                    print(f'Not enough {name} in inventory.')
                return
        print(f'Product {name} not found in inventory.')

def main():
    shopkeeper = Shopkeeper()
    print("Program started.")  # Debug print statement

    while True:
        print("\n1. Add Product")
        print("2. View Inventory")
        print("3. Record Sale")
        print("4. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            name = input("Enter product name: ")
            price = float(input("Enter product price: "))
            quantity = int(input("Enter product quantity: "))
            shopkeeper.add_product(name, price, quantity)
        elif choice == '2':
            shopkeeper.view_inventory()
        elif choice == '3':
            name = input("Enter product name: ")
            quantity = int(input("Enter quantity to sell: "))
            shopkeeper.record_sale(name, quantity)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

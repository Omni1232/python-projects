class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price
    
class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
        self.cart = Cart()

class Cart:
    def __init__(self):
        self.items = []

    def add_product(self, product):
        self.items.append(product)
        print(f"Added {product.name} to cart.")
    
    def remove_product(self, product):
        if product in self.items:
            self.items.remove(product)
            print(f"Removed {product.name} from cart.")
        else:
            print(f"{product.name} not found in cart.")

    def display_cart(self):
        print("Cart Items:")
        for product in self.items:
            print(f"{product.name} - Price: {product.get_price()}")
    
    def calculate_total(self):
        total = 0
        for product in self.items:
            total += product.get_price()
        return f"Total Price: {total}"
    
class Order:
    def __init__(self, user, items, total):
        self.user = user
        self.items = items
        self.total = total

    def display_order(self):
        print(f"Order for {self.user.name}:")
        for product in self.items:
            print(f"{product.name} - Price: {product.get_price()}")
        print(f"Total: {self.total}")

class Store:
    def __init__(self):
        self.products = {}
        self.users = {}
    
    def add_product(self):
        pid = int(input("Enter Product ID: "))
        name = input("Enter Product Name: ")
        price = float(input("Enter Product Price: "))

        self.products[pid] = Product(pid, name, price)
        print(f"Product {name} added successfully with ID {pid}.")
    
    def register_user(self):
        uid = int(input("Enter User ID: "))
        name = input("Enter User Name: ")

        self.users[uid] = User(uid, name)
        print(f"User {name} registered successfully with ID {uid}.")

    def add_to_cart(self):
        uid = int(input("Enter User ID: "))
        pid = int(input("Enter Product ID: "))

        if uid in self.users and pid in self.products:
            self.users[uid].cart.add_product(self.products[pid])
        else:
            print("Invalid User ID or Product ID.")
        
    def display_cart(self):
        uid = int(input("Enter User ID: "))
        if uid in self.users:
            self.users[uid].cart.display_cart()
        else:
            print("Invalid User ID.")

    def checkout(self):
        uid = int(input("Enter User ID: "))
        if uid in self.users:
            user = self.users[uid]
            total = user.cart.calculate_total()
            order = Order(user, user.cart.items, total)
            print("Checkout successful!")
            order.display_order()
            user.cart.items.clear()
        else:
            print("Invalid User ID.")

store = Store()

while True:
    print("\n1. Add Product")
    print("2. Register User")
    print("3. Add to Cart")
    print("4. Display Cart")
    print("5. Checkout")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        store.add_product()
    elif choice == 2:
        store.register_user()
    elif choice == 3:
        store.add_to_cart()
    elif choice == 4:
        store.display_cart()
    elif choice == 5:
        store.checkout()
    elif choice == 6:
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")

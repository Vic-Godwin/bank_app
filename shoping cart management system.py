# List of available products
products = [
    {"name": "Smartphone", "price": 400, "description": "A handheld device"},
    {"name": "Tablet", "price": 500, "description": "A handheld device with a wider screen"},
    {"name": "SmartWatch", "price": 50, "description": "A wearable device for fitness tracking"},
    {"name": "Laptop", "price": 1000, "description": "A portable computer with touchscreen functionality"},
    {"name": "Bluetooth Speaker", "price": 500, "description": "A portable speaker that connects wirelessly to devices"}
]

# Shopping cart
cart = []


# Function to display available products
def display_products():
    print("\nAvailable Products:")
    for index, product in enumerate(products):
        print(f"{index}: {product['name']} | {product['description']} | Price: ${product['price']}")
    print()


# Function to add an item to the cart
def add_to_cart():
    display_products()

    try:
        product_id = int(input("Enter the product ID to add to cart: "))
        if 0 <= product_id < len(products):
            product = products[product_id]

            # Check if product already exists in cart
            for item in cart:
                if item["name"] == product["name"]:
                    item["quantity"] += 1
                    break
            else:
                product_copy = product.copy()
                product_copy["quantity"] = 1
                cart.append(product_copy)

            print(f"\n{product['name']} has been added to the cart successfully.\n")
        else:
            print("Invalid product ID. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a number.")


# Function to view the cart
def view_cart():
    if not cart:
        print("\nYour cart is empty.\n")
        return

    print("\nYour Cart:")
    total = 0
    for item in cart:
        print(f"{item['name']} | Price: ${item['price']} | Quantity: {item['quantity']}")
        total += item['price'] * item['quantity']

    print(f"\nTotal Cost: ${total}\n")


# Function to checkout
def checkout():
    view_cart()
    if cart:
        print("Proceeding to checkout. Thank you for shopping!\n")
        cart.clear()  # Empty the cart after purchase
    else:
        print("No items in cart to checkout.")


# Main menu function
def main():
    while True:
        print("\nShopping Menu:")
        print("1. View Products")
        print("2. Add to Cart")
        print("3. View Cart")
        print("4. Checkout")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            display_products()
        elif choice == "2":
            add_to_cart()
        elif choice == "3":
            view_cart()
        elif choice == "4":
            checkout()
        elif choice == "5":
            print("Exiting... Thank you for shopping!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


# Run the program
if __name__ == "__main__":
    main()
# List of available products
products = [
    {"name": "Smartphone", "price": 400, "description": "A handheld device"},
    {"name": "Tablet", "price": 500, "description": "A handheld device with a wider screen"},
    {"name": "SmartWatch", "price": 50, "description": "A wearable device for fitness tracking"},
    {"name": "Laptop", "price": 1000, "description": "A portable computer with touchscreen functionality"},
    {"name": "Bluetooth Speaker", "price": 500, "description": "A portable speaker that connects wirelessly to devices"}
]

# Shopping cart
cart = []


# Function to display available products
def display_products():
    print("\nAvailable Products:")
    for index, product in enumerate(products):
        print(f"{index}: {product['name']} | {product['description']} | Price: ${product['price']}")
    print()


# Function to add an item to the cart
def add_to_cart():
    display_products()

    try:
        product_id = int(input("Enter the1 product ID to add to cart: "))
        if 0 <= product_id < len(products):
            product = products[product_id]

            # Check if product already exists in cart
            for item in cart:
                if item["name"] == product["name"]:
                    item["quantity"] += 1
                    break
            else:
                product_copy = product.copy()
                product_copy["quantity"] = 1
                cart.append(product_copy)

            print(f"\n{product['name']} has been added to the cart successfully.\n")
        else:
            print("Invalid product ID. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a number.")


# Function to view the cart
def view_cart():
    if not cart:
        print("\nYour cart is empty.\n")
        return

    print("\nYour Cart:")
    total = 0
    for item in cart:
        print(f"{item['name']} | Price: ${item['price']} | Quantity: {item['quantity']}")
        total += item['price'] * item['quantity']

    print(f"\nTotal Cost: ${total}\n")


# Function to checkout
def checkout():
    view_cart()
    if cart:
        print("Proceeding to checkout. Thank you for shopping!\n")
        cart.clear()  # Empty the cart after purchase
    else:
        print("No items in cart to checkout.")


# Main menu function
def main():
    while True:
        print("\nShopping Menu:")
        print("1. View Products")
        print("2. Add to Cart")
        print("3. View Cart")
        print("4. Checkout")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            display_products()
        elif choice == "2":
            add_to_cart()
        elif choice == "3":
            view_cart()
        elif choice == "4":
            checkout()
        elif choice == "5":
            print("Exiting... Thank you for shopping!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


# Run the program
if __name__ == "__main__":
    main()



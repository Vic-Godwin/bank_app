cart = []


def add_item():
    num_products = int(input("How many products do you want to add: "))

    for _ in range(num_products):
        print()
        name = input("Enter the name of the item: ")

        # Check if item is already in cart
        found = False
        for item in cart:
            if item['name'] == name:
                item['quantity'] += 1
                found = True
                break  # Stop searching since we found the item

        # If item is not in the cart, add it as a new entry
        if not found:
            des = input("Enter the description for the product: ")
            price = float(input("Enter the price of the product: "))
            item = {"name": name, "description": des, "price": price, "quantity": 1}
            cart.append(item)

        print(f"{name} successfully added to cart!\n")



# VIEW THE CART
def view_cart():

    print("AVAILABLE PRODUCTS:\n")

    for index, product in enumerate(cart):

        print(f"{index}:  {product['name']}->   {product['description']}->   ${product['price']} ->QTY= {product['quantity']}")
    total = sum(product['price'] * product['quantity'] for product in cart)
    print(f"total price of all item in cart is {total}")

# UPDATE THE CART
def update_cart():
    view_cart()
    print()
    product_id = int(input("Enter the product id you want to update: "))

    if cart[product_id] in cart:

        option = input("what do you want to update: name, price or description: ").lower()

        if option == "name":
            name = input("Enter new name: ")
            cart[product_id]['name'] = name
            print(f"Name has been updated to {cart[product_id]['name']} successfully\n")

        elif option == "price":
            price = float(input("Enter the price: "))
            cart[product_id]['price'] = price
            print(f"Price updated to ${price} successffully\n")

        elif option == "description":
            description = (input("Enter the description: "))
            cart[product_id]['description'] = description
            print(f"{cart[product_id]['name']}'s description has been updated successffully\n")
        else:
            print("Enter the proper option")
    else:
        print(f"product id: {product_id} not found")

#MAIN PROGRAM TO BE EXECUTED
def main():
    while True:
        print("""
        SHOPPING CART MANAGEMENT SYSTEM
        -------------------------------
    
        1. addd to cart
        2. view cart
        3. update cart
        4. Check Out
        5. Exit Shopping page
        """)

        try:
            choice = int(input("Enter your choice: "))
        except:
            print("INVALID Option! please Enter a valid option.")
            continue
        if choice == 1:
            add_item()

        elif choice == 2:
            view_cart()

        elif choice == 3:
            update_cart()

        elif choice == 4:
            print("Feature not yet out! ")
            main()
        elif choice == 5:
            break
        else:
            print("INVALID choice! Please Enter the right option")

#RUN THE PROGRAM
if __name__ == "__main__":
    main()
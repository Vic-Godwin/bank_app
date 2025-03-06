import time as t
import json
from ECOMMERCE_CART_DATABASE import save_user_data, load_user_data, dump_user_data

json_file = "ECOMMERCE_CART_DATABASE.json"
cart = []
def add_item():
    global json_file

    # Load existing cart data or initialize an empty list
    global cart

    num_products = int(input("How many products do you want to add: "))

    for _ in range(num_products):
        print()
        name = input("Enter the name of the item: ")

        found = False
        for item in cart:
            if item["name"] == name:  # If item exists, update quantity
                item["quantity"] += 1
                found = True
                break  # Stop searching after finding the item

        if not found:  # If item is not in cart, add a new entry
            des = input("Enter the description for the product: ")
            price = float(input("Enter the price of the product: "))
            new_item = {"name": name, "description": des, "price": price, "quantity": 1}
            cart.append(new_item)  # Add the new item to the cart

        print(f"{name} successfully added to cart!\n")

    # Save the updated cart back to the JSON file
    save_user_data(json_file, cart)




# VIEW THE CART
def view_cart():
    global json_file
    global total

    print("AVAILABLE PRODUCTS:\n")

    user_cart = load_user_data("ECOMMERCE_CART_DATABASE.json")  # Ensure it's a list

    if not user_cart:  # Check if cart is empty
        print("Your cart is empty!")
        return

    for product in user_cart:
        print(f"""
        Name:              {product['name']}
        Description:       {product['description']}
        Price:            ${product['price']}
        Quantity:          {product['quantity']}
""")

    total = sum(int(product['price']) * int(product['quantity']) for product in user_cart)
    print(f"Total price of all items in cart: ${total}")


# UPDATE THE CART
def update_cart():
    global json_file
    #view_cart()
    print()

    user_cart = list(load_user_data(json_file))
    product_name = input("Enter the product name you want to update: ")

    user_found = False
    for product in user_cart:

        if product_name == product['name']:
            des = input("Enter new Description: ")
            price = float(input("Enter new Price: "))
            product['description'] = des
            product['price'] = price
            user_found = True
            break

    if not user_found:
        print("INVALID NAME")

    with open("ECOMMERCE_CART_DATABASE.json", "w", encoding="utf_8") as file:
        json.dump(user_cart, file, indent=4)
    #3save_user_data(json_file, user_cart)




#FUNCTION INSIDE CHECKOUT
def cardCheck():
    correct = True
    user_name = input("Enter name on card: ")
    card_number = input("Enter 16-digit card number: ")

    if len(card_number) != 16 or not card_number.isdigit():
        print("INVALID CARD! It must be exactly 16 digits and contain only numbers.")
        correct = False  # Mark as incorrect if the card number is invalid

    if correct:
        card_expiry_date = input("Enter card expiry date (e.g., 0429 for 04/29): ")
        cvc = input("Enter card CVC (3-digit code on the back): ")

        if len(cvc) != 3 or not cvc.isdigit():
            print("INVALID CVC! It must be exactly 3 digits.")
            return


        user_card_detail = [{"Name": user_name, "Card Number": card_number, "Expiry Date": card_expiry_date, "CVC": cvc}]

        print()
        print(f"Processing Card information...\n")
        t.sleep(2)

        print()
        print(f"CARD DETAIL:\n|Name:{user_card_detail[0]['Name']}\n|CardNumber:{user_card_detail[0]['Card Number']}"
          f"\n|ExpiryDate:{user_card_detail[0]['Expiry Date']}\n|Card CVC:{user_card_detail[0]['CVC']}")

        print()
        print(f"Total price is ${total}")
        t.sleep(3)
        print("\nproccessing payment...")
        t.sleep(3)
        print(f"\n${total} has been successfully deducted from account!\n")

        # load the cart database from the module we created and store it as a list
        user_list = load_user_data("ECOMMERCE_CART_DATABASE.json")

        user_list = user_list.clear()
        dump_user_data("ECOMMERCE_CART_DATABASE.json", user_list)

        t.sleep(3)
        print(f"THANK YOU FOR SHOPPING! Your cart is now empty:\nSEE CART:")
        print(view_cart())





#This deletes a selected item from cart
def delete_user_item():

    user_found = False

    name = input("Enter the name of the product you want: ")

    user_list = load_user_data("ECOMMERCE_CART_DATABASE.json")

    for product in user_list:

        if product['name'] == name:
            user_list.remove(product)
            dump_user_data("ECOMMERCE_CART_DATABASE.json", user_list)
            user_found = True
            break

    if not user_found:
        print("INVALID NAME")
    #else:
        #print(f"{name} has been deleted successfully")




# CHECK OUT PAGE
def checkOut():
    card_type = input("""
    what's your card:
    1. Visa
    2. Master
    3. Verve
    4. steam
    5. more option...
    """)

    if 1 <= int(card_type) <= 4:
        t.sleep(2)
        cardCheck()

    elif card_type == "5":
        print("""
    6. apple
    7. steam
    8. alibaba
    9. previous page
    """)
        card_type = input(">>>  ")
        if card_type == "9":
            checkOut()
        else:
            cardCheck()

#MAIN PROGRAM TO BE EXECUTED
def main():
    while True:
        print("""
        SHOPPING CART MANAGEMENT SYSTEM
        -------------------------------
    
        1. addd to cart
        2. view cart
        3. update cart
        4. Remove an item from cart
        5. Check Out
        6. Exit Shopping page
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
            delete_user_item()

        elif choice == 5:
            checkOut()
        elif choice == 6:
            break
        else:
            print("INVALID choice! Please Enter the right option")
    print("Thank you for shopping!")

#RUN THE PROGRAM
if __name__ == "__main__":
    main()
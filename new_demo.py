import random


def open_account():
    global name, bvn_number, phone_number, deposit_amount, balance, acc_pin, account_numbers
    name = input("Full Name: ")
    bvn_number = input("BVN Number (11 digits): ")
    phone_number = input("Phone Number (11 digits): ")

    # Old: if len(bvn_number) and len(phone_number) != 11 or not bvn_number.isdigit() or not phone_number.isdigit():
    # Fix: Corrected validation logic
    if len(bvn_number) != 11 or len(phone_number) != 11 or not bvn_number.isdigit() or not phone_number.isdigit():
        print("INVALID BVN or PHONE NUMBER!")
        return

    deposit_amount = input("Deposit Amount: ")
    if not deposit_amount.isdigit() or int(deposit_amount) <= 0:
        print("INVALID AMOUNT! Please enter a positive number.")
        return
    deposit_amount = int(deposit_amount)

    balance = deposit_amount
    account_numbers = str(random.randint(1000000000, 9999999999))  # Generates 10-digit account number
    acc_pin = None

    print("Account Created Successfully!")
    print(f"Account Name: {name}\nAccount Number: {account_numbers}\nBalance: {balance}")


def deposit():
    global balance
    amount = input("Deposit Amount: ")

    # Old: if not deposit_amount:
    # Fix: Ensure the amount is a valid number and positive
    if not amount.isdigit() or int(amount) <= 0:
        print("INVALID AMOUNT! Please enter a positive number.")
        return

    amount = int(amount)
    balance += amount
    print(f"Deposit Successful! New Balance: {balance}")


def transfer():
    global balance
    recipient_acc_num = input("Recipient Account Number (10 digits): ")
    transfer_amount = input("Amount to Transfer: ")

    # Old: if len(recipient_acc_num) != 11 or not recipient_acc_num.isdigit():
    # Fix: Account number should be 10 digits, not 11
    if len(recipient_acc_num) != 10 or not recipient_acc_num.isdigit():
        print("INVALID ACCOUNT NUMBER!")
        return

    if not transfer_amount.isdigit() or int(transfer_amount) <= 0:
        print("INVALID TRANSFER AMOUNT!")
        return

    transfer_amount = int(transfer_amount)

    # Old: balance < transfer_amount incorrect logic
    if balance < transfer_amount:
        print("INSUFFICIENT BALANCE!")
        return

    balance -= transfer_amount
    print(f"Transfer Successful! New Balance: {balance}")


def withdraw():
    global balance
    for _ in range(3):  # Allow three attempts
        pin = input("Enter Account PIN: ")
        if pin == acc_pin:
            break
        else:
            print("Incorrect PIN. Try again.")
    else:
        print("Too many incorrect attempts. Withdrawal canceled.")
        return

    withdraw_amount = input("Withdrawal Amount: ")
    if not withdraw_amount.isdigit() or int(withdraw_amount) <= 0:
        print("INVALID AMOUNT!")
        return

    withdraw_amount = int(withdraw_amount)

    if balance < withdraw_amount:
        print("INSUFFICIENT BALANCE!")
        return

    balance -= withdraw_amount
    print(f"Withdrawal Successful! New Balance: {balance}")


def set_up_pin():
    global acc_pin

    # Old: if pin == acc_pin or len(acc_pin) == 4:
    # Fix: Properly check if PIN is already set
    if acc_pin:
        print(f"You've already set a PIN: {acc_pin}")
        return

    acc_pin = input("Set a 4-digit PIN: ")
    if len(acc_pin) != 4 or not acc_pin.isdigit():
        print("INVALID PIN! Please enter exactly 4 digits.")
        acc_pin = None
        return

    print("PIN Set Successfully!")


def check_balance():
    print(f"Your Current Balance is: {balance}")


def display_account_details():
    print(
        f"Name: {name}\nBVN: {bvn_number}\nPhone: {phone_number}\nAccount Number: {account_numbers}\nBalance: {balance}")

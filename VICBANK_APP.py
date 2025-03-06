import random
import time as T
from VICBANK_MODULE import save_user_data as save, load_user_data as load, dump_user_data as dump

account_numbers = [str(random.randint(1000000000, 9999999999)) for _ in range(500)]
account_number = random.choice(account_numbers)

"""
open account
deposit money
set up pin
transfer
Withdraw
check account balance
account detail
"""
balance = 0
bank_name = 'VICBANK'
data_file_path = "VICBANK_DATABASE.json"
acc_pin = ''
user_data = []
copy_name = ''


# THIS FUNCTION ENABLES USERS TO CREATE AN ACCOUNT
def open_acount():
    global copy_name
    correct = True

    print("YOUR DETAILS\n")

    name = input("Enter your fullname: ")

    if name == copy_name:
        print("Account Already exist")
        correct = False

    if correct:
        gender = input("Enter Gender info (M for male, F for female) or spell out: ")
        marital_status = input("What's your marital status: single, married, widow, widower: ")
        date_of_birth = input("Enter date of birth(day/month/year): ")
        state_residence = input("what's your state of residence: ")
        state_origin = input("What's your state of origin: ")
        email = input("Enter Email Address: ")
        phone_number = input("Enter your phone number: ")
        bvn_number = input("Enter your BVN: ")

        if len(bvn_number) != 11 or len(phone_number) != 11 or not bvn_number.isdigit() or not phone_number.isdigit():
            print("INVALID BVN or PHONE NUMBER: Both must be exactly 10 digits and contains only number")
            correct = False

        if correct:

            nin_number = input("Enter 15 digit NIN number: ")

            if len(nin_number) != 15 or not nin_number.isdigit():
                print("INVALID NIN! It must be exactly 15 digits and contain only numbers.")
                correct = False

            if correct:
                T.sleep(1.5)
                print("\nSaving data...\n")
                T.sleep(1.5)

                print("NEXT OF KIN DETAIL\n")  # NEXT OF KIN INFORMATION

                T.sleep(1)
                name2 = input("Enter their fullname of next of kin: ")
                relationship = input("What's your relation with this person: Brother, sister, father.. ")
                gender2 = input("Enter enter their gender(M for male, F for female): ")
                date_of_birth2 = input("Enter their date of birth(day/month/year): ")
                state_residence2 = input("what's their state of residence: ")
                phone_number2 = input("Enter Phone Number: ")

                T.sleep(1)
                print("\nSaving data...\n")
                T.sleep(1.5)

                print("processing data...\n")
                T.sleep(.8)

                print("Checking Validity of information\n")
                T.sleep(1.)

                print(F"""
        DEAR {name.upper()} YOUR ACCOUNT HAS BEEN SUCCESSFULLY CREATED

        THANK YOU FOR CHOOSING {bank_name}.

        You'll receive an sms with account number and detail soon\n""")

                store_info = {"name": name.upper(),"marital status": marital_status.upper(),
                              "gender": gender.upper(), "email": email,
                              "state of residence": state_residence.upper(),
                              "state of origin": state_origin.upper(),
                              "date of birth": date_of_birth, "phone number":phone_number,
                              "BVN":bvn_number,"NIN":nin_number,
                              "account number": account_number,"account balance": balance
                              }

                next_of_kin = {"name": name2, "phone number": phone_number2,
                               "gender": gender2, "Relationship": relationship,
                               "state of residence": state_residence2, "date of birth": date_of_birth2}

                copy_name = name
                user_data.append(store_info)
                save(data_file_path, user_data)
                input("Click Enter to continue ")


# THIS FUNCTION ALLOWS THE USER TO DEPOSIT MONEY TO THEIR ACCOUNT
def deposit():
    global balance

    deposit_amount = input("Enter the amount in dollars you want to deposit: ")

    if not deposit_amount.isdigit() or int(deposit_amount) <= 0:
        print("INVALID AMOUNT: Please Enter a valid amount")
        return

    acc_number = input("Enter Account Number: ")

    if not acc_number.isdigit() or len(acc_number) != 10:
        print("INVALID ACCOUNT NUMBER. ONLY NUMBERS")
        return

    if acc_number == account_number:

        print("\nsearching account name...")
        T.sleep(3)

        print(f"\nAccount name: {user_data[0]['name']}\n")
        T.sleep(1)

        input("Click Enter to confirm name")
        T.sleep(2)

        print("processing transaction...\n")
        T.sleep(3)

        deposit_amount = int(deposit_amount)

        balance = balance + deposit_amount
        print("TRANSACTION SUCCESSFULLY!")
        T.sleep(2)

        print(f"Your VICBANK account has been credited with ${balance}\n")
        input("Click Enter to continue ")

    else:
        print("Account number was not found")


# THIS FUNCTION ALLOWS THE USER TO SET UP THEIR TRANSACTION PIN
def set_up_pin():
    global acc_pin

    correct = True

    print(f"""
    Set up your {bank_name} transaction pin in a MINUTE
    PLEASE NO THAT YOU HAVE ONLY 3 TRIALS TO CONFIRM PIN\n
""")

    for _ in range(3):

        pin = input("Enter A 4-digit pin: ")

        if pin == acc_pin or len(acc_pin) == 4:
            print(f"You've already have a pin: your pin is {acc_pin}")
            return

        confirm_pin = input("Confirm Pin: ")

        if pin != confirm_pin:
            print("PIN DIDN'T MATCH")
            correct = False
            continue

        if correct:
            pin1 = ''
            acc_pin = pin1 + pin

            T.sleep(1)
            print("TRANSACTION PIN has been created successfully created\n")

            print(f"{acc_pin} is your transaction pin: for withdrawal and transfer\n")

            input("click Enter to continue ")
            break


# THIS FUNCTION HELPS CUSTOMERS TO TRANSFER MONEY TO OTHER BANKS OR WITHIN VICBANK
def transfer():
    global balance

    correct = True

    pin = acc_pin

    if len(pin) < 1:
        print("PLEASE SET UP ACCOUNT PIN FIRST!")
        correct = False

    if correct:
        print(f"Your about to transfer money from your {bank_name} acount\n")

        recipient_acc_num = input("Enter receiver's account number: ")

        if len(recipient_acc_num) != 10 or not recipient_acc_num.isdigit():
            print("\nINVALID ACCOUNT NUMBER. number must be 10 digit and must contain only number")
            return

        print(f"\nCHECKING FOR {bank_name} USER WITH ACCOUNT {recipient_acc_num}")
        T.sleep(2)

        name_user = ['Mary bent', 'John Trump', 'Eva Martin', 'Victor Godwin']
        user = random.choice(name_user)

        print(f"Found: {user}\nclick enter to confirm\n")
        input()

        transfer_amount = input("Enter the amount: ")

        if not transfer_amount.isdigit() or int(transfer_amount) <= 0:
            print("\nINVALID AMOUNT! Enter a valid amount")
            return

        your_pin = input("Enter your VICBANK Transfer pin: ")

        if your_pin != acc_pin:
            print("INVALID PIN. PLEASE CHECK YOUR PIN PROPERLY.")
            return

        transfer_amount = int(transfer_amount)

        if balance < transfer_amount:
            print("INSUFFICIENT BALANCE! ")
            correct = False

        if correct:
            balance = balance - transfer_amount

            print("\nPROCESSING TRANSFER...")
            T.sleep(3)

            print("TRANSFER SUCCESSFUL\n")
            T.sleep(.4)

            print(f"Your {bank_name} acount balance is ${balance}\n")
            input("Click Enter to Continue: ")


# THIS FUNCTION ENABLES CUSTOMERS TO WITHDRAW THEIR MONEY
def withdraw():
    global balance

    correct = True

    print(f"You're about to withdraw from your {bank_name} account\n")

    withrawal_amount = input("Enter the amount to Withdraw: ")

    if not withrawal_amount.isdigit() or int(withrawal_amount) <= 0:
        print("\nINVALID AMOUNT: PLEASE ENTER a valid amount!")
        return

    withrawal_amount = int(withrawal_amount)

    if balance < withrawal_amount:
        print(f"\nINSUFFICIENT BALANCE. Try a smaller amount")
    else:
        balance = balance - withrawal_amount

        for _ in range(3):
            pin = input("Account Pin (MAKE SURE TO CHECK PIN). only 3 trials: ")
            if acc_pin == pin:
                correct = True
                break

            if not correct:
                continue

            print("\nProcessing withdraw. please be patient and don't interrupt the process")
            T.sleep(3)

            print(f"\n${withrawal_amount} has been successfully withdrawn from account!\n")
            T.sleep(1.6)

            print(f"Your balance is ${balance}\n")
            input("Click Enter to continue: ")


# THIS FUNCTION SHOWS THE ACCOUNT BALANCE OF THE REGISTERED ACCOUNT
def acc_balance():
    print("""

    CHECKING ACCOUNT BALANCE...\n""")
    T.sleep(3)

    print(f"""
    ==================================
    |Account balance:       ${balance}
    ==================================
    \n""")
    input("Click Enter to continue ")


# THIS FUNCTION GETS THE ACCOUNT INFORMATION OF CUSTOMER
def acc_info():
    print("GETTING ACCOUT INFORMATION...\n")
    T.sleep(2)

    print("YOUR ACCOUNT DETAIL:\n")

    for info in user_data:
        print(f"""
    ============================    
        ACCOUNT INFORMATION
    =============================

    |Name:                   {info['name'].upper()}
    |Marital Status:         {info['marital status'].upper()}
    |Gender:                 {info['gender'].upper()}
    |Date Of Birth:          {info['date of birth']}
    |State of residence:     {info['state of residence'].upper()}
    |Phone Number:           {info['phone number']}
    |Email:                  {info['email']}
    |State Of Origin:        {info['state of origin'].upper()}
    |BVN:                    {info['BVN']}
    |NIN:                    {info['NIN']}

    |Account Number:         {account_number}

    ------------------------------------
    ACCOUNT BALANCE:        ${balance}
    ------------------------------------
\n""")

    print("Make sure to copy Account number\n")
    input("Click Enter to Continue")


while True:

    print(f"""
    WELCOME TO {bank_name}: THE BEST IN THE COUNTRY


    Please! set up pin before transfer
    write your account number down for deposit
    you'll need those information later

    1. Open Account
    2. Deposit
    3. Set up transaction pin
    4. Transfer
    5. Withdraw
    6. Check Balance
    7. Account information
    8. Close transaction
    \n""")

    choice = input("Chose your choice: ")

    if choice == "1":
        open_acount()

    elif choice == "2":
        deposit()

    elif choice == "3":
        set_up_pin()

    elif choice == "4":
        transfer()

    elif choice == "5":
        withdraw()

    elif choice == "6":
        acc_balance()

    elif choice == "7":
        acc_info()

    elif choice == "8":
        print("THANk YOU FOR BANKING WITH US!")
        break
    else:
        print("INVALID OPTION")
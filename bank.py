balance = 0
history = []

# --- Open the account ---
while True:
    try:
        n = float(input("\nEnter some amount to open the account in the bank: "))
        if n > 0:
            balance = n
            print("\nYour account is opened successfully in the bank!")
            print("Now you can access your account. ==>")
            history.append("Amount when open the account: ₹"+ str(n))
            break
        else:
            print("\nError — please enter the valid amount...try again...")
    except ValueError:
        print("\nError — please enter a valid number!")

# --- Bank Menu ---

while True:
    print("\n===== BANK MENU =====")
    print("1. Deposit Money")
    print("2. Withdraw Money")
    print("3. Check Balance")
    print("4. Transaction History")
    print("5. Exit")

    choice = input("\nEnter your choice (1-5): ")

    # Deposit money

    if choice == '1':
        try:
            amount = float(input("\nEnter amount to deposit: "))
            if amount > 0:
                balance += amount
                history.append("Deposited: ₹" + str(amount))
                print("\nAmount deposited successfully!")
            else:
                print("\nError — amount should be greater than zero!")
        except ValueError:
            print("\nInvalid input! Please enter a numeric value.")

    # Withdraw money

    elif choice == '2':
        try:
            amount = float(input("\nEnter amount to withdraw: "))
            if amount > 0:
                if amount <= balance:
                    balance -= amount
                    history.append("Withdrawn: ₹" + str(amount))
                    print("\nAmount withdrawn successfully!")
                else:
                    print("\nInsufficient balance!")
            else:
                print("\nError — amount should be greater than zero!")
        except ValueError:
            print("\nInvalid input! Please enter a numeric value.")

    # Check balance

    elif choice == '3':
        print("\nYour current balance is: ₹", balance)

    # Transaction history

    elif choice == '4':
        print("\n===== Transaction History =====")
        if not history:
            print("No transactions yet.")
        else:
            for record in history:
                print(record)
                
    # Exiting from the bank

    elif choice == '5':
        print("\nThank you for using our Bank System! ")
        break

    else:
        print("\nInvalid choice! Please enter a number between 1-5.")
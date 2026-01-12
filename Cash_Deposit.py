def deposit(balance):
    deposit_amount = int(input("Enter amount to deposit: "))
    if deposit_amount > 0:
        balance += deposit_amount
        print("Deposit successful")
        print("Your new balance is:", balance)
    else:
        print("Invalid deposit amount")
    return balance
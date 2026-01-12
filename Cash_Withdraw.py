def withdraw(current_balance):
    amount = float(input('amount to withdraw:'))
    if amount <= 0:
        print("Error: Withdrawal amount must be positive.")
        return current_balance
    if amount > current_balance:
        print(f"Transaction Denied: Insufficient funds.")
        print(f"Requested: ${amount:,.2f} | Available: ${current_balance:,.2f}")
        return current_balance
    new_balance = current_balance - amount
    print(f"--- Withdrawal Successful ---")
    print(f"Dispensing: ${amount:,.2f}")
    print(f"New Balance: ${new_balance:,.2f}")
    return new_balance


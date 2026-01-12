#This part deals with user account creation for the ATM
import csv
import random
option = ''
current_user = ''  # To track the logged-in user

def update_balance(username, new_balance):
    rows = []
    with open('users.csv', mode='r') as file:
        reader = csv.reader(file, delimiter=',')
        for row in reader:
            if row[0] == username:
                row[3] = str(new_balance)  # Update balance
            rows.append(row)
    with open('users.csv', mode='w', newline='') as file:
        writer = csv.writer(file, delimiter=',')
        writer.writerows(rows)
def entrance(x):
    global pin, balance1
    x = input("Do you have an account with us? (yes/no): ").strip().lower()
    if x == 'no':
        while True:
            print("Let's create an account for you.")
            username = str(input("Enter the username you would like to use:")).lower()
            with open('users.csv', mode='r') as file:
                reader = csv.reader(file, delimiter=',')
                username_exists = False
                for row in reader:
                    if row[0] == username:
                        username_exists = True
                        break
            if username_exists:
                print("Username already exists. Please choose another.")
                continue
            password = input("Enter your password it must be at least five characters long:")
            if len(password) < 5:
                print('Too short must be more than five characters')
                continue
            else:
                password2 = input('Re-enter your password:')
                if password == password2:
                    balance1 = 0
                    pin = random.randint(1000, 9999)
                    print(f"Your generated pin is: {pin}. Please remember it for future logins.")
                    with open('users.csv', mode='a', newline='') as file:
                        writer = csv.writer(file, delimiter=',')
                        writer.writerow([username,password,pin,balance1])
                    break
                else:
                    print("Passwords do not match. Please try again.")
                    continue
    if x == 'yes':
        print("Welcome back please enter your username and password")
        usernametoenter= str(input("Please enter your username:"))
        passwordtoenter= str(input("Please enter your password:"))
        pintoenter= str(input("Please enter your pin:"))
        with open('users.csv', mode='r') as file:
            reader = csv.reader(file, delimiter=',')
            logged_in = False
            for row in reader:
                if row[0] == usernametoenter and row[1] == passwordtoenter and row[2] == pintoenter:
                    pin = int(row[2])
                    balance1 = int(row[3])
                    current_user = usernametoenter  # Store the username
                    print("You are logged in")
                    logged_in = True
                    break
            if not logged_in:
                print("Invalid credentials")
entrance(option)
accounts = {}
accounts.update({pin: balance1})
print(accounts)
print("What would you like to do")
selection = input(" B to deposit cash, C to check balance and D to withdraw cash").upper()


given_pin = int(input("Please enter your pin:"))
if given_pin not in accounts:
    print("Invalid pin")
else:
    if selection == "B":
        import Cash_Deposit
        accounts[given_pin] = Cash_Deposit.deposit(accounts[given_pin])
        update_balance(current_user, accounts[given_pin])  # Update the balance in CSV
    elif selection == "C":
        print("Your balance is:", accounts[given_pin])







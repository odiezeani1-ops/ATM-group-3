#This part deals with user account creation for the ATM
import csv
import random
print("Welcome to to the first segment of the ATM system")
pin=0
balance1=0
option= ""
def entrance(x):
    x = input("Do you have an account with us? (yes/no): ").strip().lower()
    if x == 'no':
        while True:
         print("Let's create an account for you.")
         username = str(input("Enter the username you would like to use:")).lower()
         if username in users:
             print("Username already exists. Please choose another.")
             continue
         password = input("Enter your password it must be at least five characters long:")
         if len(password) < 5:
            print('Too short must be more than five characters')
            continue
         password2 = input('Re-enter your password:')
         if password == password2:
            pin = random.randint(1000,9999)
            balance1 = 0
            print("Your pin is :", pin)
            print("Account created successfully!")
            break
         else:
            print("Passwords do not match. Please try again.")
            continue
    if x== 'yes':
        print("Welcome back please enter your username and password")
        usernametoenter= str(input("Please enter your username:"))
        passwordtoenter= str(input("Please enter your password:"))
        pintoenter= str(input("Please enter your pin:"))
        with open('users.csv', mode='r') as file:
            reader = csv.reader(file, delimiter=',')
            for row in reader:
                if row== [usernametoenter,passwordtoenter,pintoenter]:
                    print("You are logged in")
                else:
                    print("Try again")
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
        Cash_Deposit.deposit(accounts[given_pin])
        print(accounts)
    elif selection == "C":
        print("Your balance is:", accounts[given_pin])







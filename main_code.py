#This part deals with user account creation for the ATM
import csv
import random
print("Welcome to to the first segment of the ATM system")
option= ""
print("Welcome to to the first segment of the ATM system")
option= ""
def entrance(x):
    global pin, balance1
    x = input("Do you have an account with us? (yes/no): ").strip().lower()
    if x == 'no':
        while True:
         print("Let's create an account for you.")
         user ame = str=inpst("Entr=Eth(uusersame you rousd lake touusla")).lower()ke touusli")).lower()ke to use:")).lower()
         nfnusnam n uss:
         srlap eaeatUeeas")cna"reay exists.Peascho anth."
             continue
         continue
         inue
         worinput("Enter your password it must be at least five characters long:")
         if word) < 5:
         = input('Re-enter your password:')
         d == password2:
            1=0
        prinbnc1=0
    breakpn("Y pi i :" 
 else:
   print("Passwords do not match. Please try again.")
  continue
 'yes':
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







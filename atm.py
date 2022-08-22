"""
This program is simulate an ATM banking machine. The program will first ask for the user’s PIN code. The user has 3
attempts to enter their PIN. If the PIN is entered incorrectly 3 times the program will output a message to the effect
that the card has been retained and should then restart. If the PIN code is entered correctly, the user will be able to
•  Check their balance
•  Withdraw money from their account up to the total of their balance
•  Deposit money into the account
The user’s balance at the beginning of the transaction will be a randomly generated total between £100 - £1000.
"""

from random import randrange  # import extra module (randrange from random module)

password = 1234  # create a PIN number
balance = float(randrange(100, 1001))  # randomly create a balance in the range 100 and 1000


# PIN function
def pin_function():
    count = 3  # number of chances to enter PIN number

    while True:  # create a loop for the user to enter the password
        user = int(input("Enter your (4 numbers) PIN password: "))  # ask the user for the PIN number
        # if the input is not 4 numbers
        if len(str(user)) != 4:  # if the input is not 4 characters
            print("That's not 4 numbers.\nTry again.")

        # if the PIN number is correct
        elif user == password:
            print("Welcome back!")
            break

        # if the PIN number is not correct
        elif user != password:
            count -= 1
            print("Wrong password\nYou have", count, "chance(s) left.")

            # if the user enter 3 times incorrectly
            if count == 0:
                print("\nYour card has been retained.\nYou have to restart the program.\n")
                count = 3
                continue

    return count  # return the output of the function (number of chances for the program)


# ATM withdraw function
def withdraw_money(person_balance):
    # ask the user for the amount of money he/she wants to withdraw
    withdraw = float(input("The money you want to withdraw: "))
    # if the amount of money he/she wants to withdraw is lower their bank account (accepted)
    if withdraw < person_balance:
        person_balance -= withdraw  # minus the balance by the amount of money the user wants to withdraw
        print("\nYou have withdrawn: " + str(withdraw) + "£")
    # if the amount of money he/she wants to withdraw is over their bank account (unaccepted)
    else:
        print("The amount you want to withdraw is over your balance.\nPlease try again.")
    return person_balance  # return the output of the function (the new balance)


# ATM deposit function
def deposit_money(person_balance):
    # ask the user for the amount of money he/she wants to deposit
    deposit = float(input("How much you want to deposit: "))
    person_balance += deposit  # add the balance with the amount of money the user wants to deposit
    print("\nYou have deposited: " + str(deposit) + "£.")
    return person_balance  # return the output of the function (the new balance)


# ATM start
chances = pin_function()  # run the pin_function to log in

# ATM functions
# Create a loop for the user to withdraw of deposit the money
while chances != 0:  # while the user enter the PIN password correctly
    print("Your balance is:", "£" + str(balance), "\n")  # print the current balance
    # provide user with multiple choices
    decision = str(input("How can I help you?\n1. Withdraw money\n2. Deposit money\nEnter \"stop\" when you finish.\n"))

    # if the user choose to withdraw money
    if decision == "1" or decision.lower() == "withdraw money":
        balance = withdraw_money(balance)
        continue

    # if the user choose to deposit money
    elif decision == "2" or decision.lower() == "deposit money":
        balance = deposit_money(balance)
        continue

    # if the user wants to end the program
    elif decision.lower() == "stop":
        print("Thank you very much.")
        break

    # if the user enter an invalid syntax
    else:
        print("Try again.")
        continue

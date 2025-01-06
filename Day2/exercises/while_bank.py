#bank account
balance = 0
while True:
    user_input = int(input("Press number. \n0: check the balance // 1: quit\n"))
    if user_input == 0:
        print("Your balance is", balance)
        deposit_input = int(input("Do you want to deposit or withdraw money?\n1: deposit // 2: withdraw // 3: quit\n"))
        if deposit_input == 1:
            money = int(input("How much do you want to add to your account?\n"))
            balance += money
            print("Now your balance is", balance)
        elif deposit_input == 2:
            money = int(input("How much do you want to withdraw from your account?\n"))
            if money > balance:
                print("You don't have enough money.")
                continue
            balance -= money
            print("Now your balance is", balance)
        elif deposit_input == 3:
            continue
        else:
            print("Please press valid number.")
            continue
    elif user_input == 1:
        print("Thank you! Buy!")
        break
    else:
        print("Please press valid number.")


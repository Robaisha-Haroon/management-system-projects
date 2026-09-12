# combining OOPs and Dictionary concept 

class BankAccount:
    def create_account(self, name, pin, initial_amount):
        self.name = name
        self.pin = pin
        self.initial_amount = initial_amount
        print(f"Account for {self.name} has been made successfully")
        
    def deposit(self, amount):
        self.amount = amount
        self.initial_amount += self.amount
        print(f"{self.amount} amount has been deposit successfully")
        
    def withdraw(self, withdraw_amount):
        self.withdraw_amount = withdraw_amount
        self.initial_amount -= self.withdraw_amount
        print(f"{self.withdraw_amount} amount has been withdraw successfully")
        
    def check_balance(self):
        print(f"Your balance is {self.initial_amount}")

user_account = BankAccount()
account = {}
create_account = False
print("=========== Welcome To Your ATM Account =========== \n")
while True:
    try:
        choice = int(input("""What would you like to do?
        1. Create an account
        2. Log in to an account
        3. Deposit the cash
        4. Withdrawl the cash
        5. Check balance
        6. Log Out/Exit\n"""))
        
        if choice == 1:
            try:
                name = input("Enter the username: ").strip()
                if name in account:
                    print("Username already exists")
                    continue
                input_pin = input("Enter the 4 digit Pin: ")
                if len(input_pin) != 4 or not input_pin.isdigit():
                    print("Pin must contain 4 digiis")
                    continue
                else:
                    pin = int(input_pin)
                amount = int(input("Enter the amount: "))
                if amount >= 0:
                    create_account = True
                    
                    account[name] = {
                        "Pin": pin,
                        "Balance": amount
                    }
                    
                    user_account.create_account(name, pin, amount)
                else:
                    print("Invalid amount")
            except ValueError:
                print("Invalid username or Pin or amount")

        elif choice == 2:
            try:
                username = input("Enter the username")
                if username in account:
                    log_in= int(input("Enter the 4 digit Pin"))
                    if log_in == account[username]["Pin"]:
                        print("LOG IN SUCCESSFULLY")
                    else:
                        print("Wrong Pin")
                else:
                    print("This account doesn't exist")
            except ValueError:
                print("Invalid username or Pin")
        elif choice == 3:
            if create_account == True:
                try:
                    ask = int(input("Enter the deposit amount: "))
                    if ask >= 0:
                        user_account.deposit(ask)
                        account[name]["Balance"] = user_account.initial_amount   
                    else:
                        print("Invalid amount")
                except ValueError:
                    print("Invalid deposit amount")
            else:
                print("Create account First")      
                
        elif choice == 4:
            if create_account == True:
                try:
                    withdrawl = int(input("Enter the withdrawl amount: "))
                    if withdrawl >= 0 and withdrawl <= user_account.initial_amount:
                        user_account.withdraw(withdrawl)
                        account[name]["Balance"] = user_account.initial_amount
                    else:
                        print("Invalid amount")
                except ValueError:
                    print("Invalid withdrawl amount")
            else:
                print("Create account First")
                
        elif choice == 5:
            if create_account == True:
                user_account.check_balance()
            else:
                print("Create account First")
                
        elif choice == 6:
            print("Thank you for Visiting")
            break
        else:
            print("Invalid choice. Choose between 1 to 5")    
    except ValueError:
        print("Invalid choice. Choose between 1 to 5")

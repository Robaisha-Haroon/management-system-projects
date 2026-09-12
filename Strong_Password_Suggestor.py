# Strong password generator with functions

def strong(password):
    symbol = "!@#$%^&*()_+-{}[]:'\<>?,./"
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    number = "1234567890"
    
    if len(password) < 8:
        return "The length of the Password should be equal or greater than 8"
    if not any(i in symbol for i in password):
        return "Add at least one symbol"
    elif not any(i in alphabet for i in password):
        return "Add at least one alphabet"
    elif not any(i in number for i in password):
        return "At least add one number"
    else:
        return "Password successfully added!"

username = input("Enter your username: ")
while True:
    password = input("Enter the password: ")
    
    security = strong(password)
    print(security) 
    
    if security == "Password successfully added!":
        print("Welcome", username)
        break

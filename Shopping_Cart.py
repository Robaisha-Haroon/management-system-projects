# Shopping Cart

# Initialize cart and store database
cart_items = []
cart_prices = []

# Store inventory and prices
store_inventory = {
    "Book": 200,
    "Laptop": 2000,
    "Headphones": 1500
}

# User Onboarding
name = input("Enter Your Good name: ").strip().capitalize()
print(f"\nHello... {name}, Welcome to the Quickserver store!")
print("What would you like to buy?")
for item, price in store_inventory.items():
    print(f" - {item}: Rs {price}")

# Shopping Loop
for item_name, item_price in store_inventory.items():
    user_choice = input(f"\nDo you want to buy a {item_name.lower()}? (Yes/No): ").strip().capitalize()
    
    if user_choice == "Yes":
        try:
            quantity = int(input("Enter the quantity as a number: "))
            if quantity > 0:
                cart_items.append(f"{item_name} (x{quantity})")
                cart_prices.append(quantity * item_price)
            else:
                print("Quantity must be greater than 0.")
        except ValueError:
            print("Invalid input! Please enter a valid number next time.")
    elif user_choice == "No":
        print("Okay.")
    else:
        print("Invalid option selected.")

# Checkout and Billing
see_bill = input("\nDo you want to see the bill? (Yes/No): ").strip().capitalize()

if see_bill == "Yes":
    total_bill = sum(cart_prices)
    
    # Discount Logic
    if total_bill >= 3000:
        total_bill *= 0.9
        print("\n🎉 You get a 10% discount!")
    else:
        shortfall = 3000 - total_bill
        print(f"\nYou got no discount. To avail the discount, you have to spend Rs: {shortfall} more.")
    
    # Final Receipt Display
    print("\n" + "="*30)
    print("✨ FINAL RECEIPT ✨")
    print("="*30)
    print("Your total items are:", ", ".join(cart_items) if cart_items else "None")
    print(f"Total Bill: Rs: {total_bill:.2f}")
    print("="*30)
else:
    print("\nI think you are very rich!")

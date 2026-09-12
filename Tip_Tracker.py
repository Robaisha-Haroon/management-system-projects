# Tip tracker

def total_tip(bill, tip_value=15):
    give_tip = bill* (tip_value/100)
    return give_tip
def final_bill(bill, give_tip):
    total_bill = bill + give_tip
    return total_bill
def bill_splitter(total_bill, friends):
    bill_splitter = total_bill / friends
    return bill_splitter

number_of_people= int(input("Enter how many people are there?\n"))

before_tip = int(input("Enter how much is your bill?\n"))

tip= total_tip(before_tip)

final_bill = final_bill(before_tip, tip)

bill_split= bill_splitter(final_bill, number_of_people)

while True:
    ask= int(input("""enter what you want to see?
        1. Bill before tip
        2. Tip you are giving
        3. Total Bill
        4. Total Bill split between people
        5. Exit\n"""))
    if ask == 1:
        print("Your bill before tip is", before_tip)
    elif ask == 2:
        print("you are giving", tip, "as tip")
    elif ask == 3:
        print("Your total bill is", final_bill)
    elif ask == 4:
        print("among the", number_of_people, "people, each person need to give", round(bill_split))
    elif ask == 5:
        print("Thank you for visiting")
        break
    else:
        print("Invalid choice. Choose between 1 to 4")

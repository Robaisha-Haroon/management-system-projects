# Budget Buddy

def calculate_saving(income, expense):
    savings= income - expense
    return savings
def saving_percentage(income, saving):
    percentage_saving= (saving/income)*100
    return percentage_saving
def get_financial_status(percentage_saving, income):
    if percentage_saving <= 0:
        return "Overspending"
    elif percentage_saving <= 20:
        return "Tight Budget"
    elif percentage_saving >= 20  and percentage_saving < 50:
        return "Safe Zone"
    elif percentage_saving >= 50:
        return "Super Saving!"
    else:
        return "Invalid number"

salary= int(input("Enter your income\n"))
expense= int(input("Enter your bill or expense\n"))
saved= calculate_saving(salary, expense)
percent_save= saving_percentage(salary, saved)
print("You had saved", round(saved), "YOU had saved", round(percent_save,2), "From your salary")
print("Your Financial status is", get_financial_status(percent_save, salary))

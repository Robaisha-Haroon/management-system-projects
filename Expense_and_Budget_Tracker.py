# expense and budget tracker

ideal_expense = {}
actual_expense = {}

# Variables for ideal_expense dictionary
salary = int(input("Enter your salary: "))
month = input("Enter month and year: ")

ideal_bill_budget = salary * 0.4
ideal_shopping_budget = salary * 0.2
ideal_outing_budget = salary * 0.2
ideal_saving = salary * 0.2

ideal_expense[month] = {
    "Salary": salary,
    "Bill": ideal_bill_budget,
    "Shopping": ideal_shopping_budget,
    "Outing": ideal_outing_budget,
    "Saving": ideal_saving
}

actual_expense[month] = {
    "Bill Spend": 0,
    "Shopping Spend": 0,
    "Outing Spend": 0,
    "Took From Savings": 0
}

# Variables for Financial Summary
bill_budget = ideal_expense[month]["Bill"]
shopping_budget = ideal_expense[month]["Shopping"]
outing_budget = ideal_expense[month]["Outing"]
saving_budget = ideal_expense[month]["Saving"]

while True:
    print("\n======== Expense And Budget Tracker ========")

    # Mega condition
    try:
        choice = int(input("""Enter what you want to do?
        1. Add Expense
        2. View Actual Expenses
        3. View Budget
        4. View Financial Summary
        5. View Category
        6. Exit
        Choice: """))

    except ValueError:
        print("Choose number between 1-6")
        continue

    # First condition
    if choice == 1:

        try:
            want = int(input("""Enter from what you want to add expense
        1. On Bill
        2. On Shopping
        3. On Outing
        4. From Saving
        5. Exit
        Choice: """))

        except ValueError:
            print("Only numbers are valid")
            continue

        if want == 1:

            try:
                spend_bill = int(input("Enter how much you had spend on bills?\n"))

                if spend_bill > 0:

                    total_bill_spend = actual_expense[month]["Bill Spend"] + spend_bill
                    actual_expense[month]["Bill Spend"] += spend_bill

                    if total_bill_spend <= ideal_bill_budget:
                        print("Expense has been added")

                    else:
                        out_of_budget_bill = total_bill_spend - ideal_bill_budget
                        print("Expense has been added")
                        print("You have exceeded your bill budget by", out_of_budget_bill)

                else:
                    print("Invalid number")

            except ValueError:
                print("Only numbers are valid")

        elif want == 2:

            try:
                spend_shopping = int(input("Enter how much you had spend on shopping?\n"))

                if spend_shopping > 0:

                    total_shopping_spend = actual_expense[month]["Shopping Spend"] + spend_shopping
                    actual_expense[month]["Shopping Spend"] += spend_shopping

                    if total_shopping_spend <= ideal_shopping_budget:
                        print("Expense has been added")

                    else:
                        out_of_budget_shopping = total_shopping_spend - ideal_shopping_budget
                        print("Expense has been added")
                        print("You have exceeded your shopping budget by", out_of_budget_shopping)

                else:
                    print("Invalid number")

            except ValueError:
                print("Only numbers are valid")

        elif want == 3:

            try:
                spend_outing = int(input("Enter how much you had spend on outing?\n"))

                if spend_outing > 0:

                    total_outing_spend = actual_expense[month]["Outing Spend"] + spend_outing
                    actual_expense[month]["Outing Spend"] += spend_outing

                    if total_outing_spend <= ideal_outing_budget:
                        print("Expense has been added")

                    else:
                        out_of_budget_outing = total_outing_spend - ideal_outing_budget
                        print("Expense has been added")
                        print("You have exceeded your outing budget by", out_of_budget_outing)

                else:
                    print("Invalid number")

            except ValueError:
                print("Only numbers are valid")

        elif want == 4:

            try:
                spend_saving = int(input("Enter how much you had spend?\n"))

                if spend_saving > 0:

                    total_saving_spend = actual_expense[month]["Took From Savings"] + spend_saving
                    actual_expense[month]["Took From Savings"] += spend_saving

                    if total_saving_spend <= ideal_saving:
                        print("Expense has been added")

                    else:
                        out_of_saving = total_saving_spend - ideal_saving
                        print("Amount has been added")
                        print("You have exceeded your saving budget by", out_of_saving)

                else:
                    print("Invalid number")

            except ValueError:
                print("Only numbers are valid")

        elif want == 5:
            continue

        else:
            print("Choose between 1-5")

    # second condition
    elif choice == 2:

        print("\n===== Actual Expenses =====")

        for i, j in actual_expense[month].items():
            print(i, ":", j)

    # third condition
    elif choice == 3:

        print("\n===== Ideal Budget =====")

        for i, j in ideal_expense[month].items():
            print(i, ":", j)

    # fourth condition
    elif choice == 4:

        # Get latest expenses
        bill_spend = actual_expense[month]["Bill Spend"]
        shopping_spend = actual_expense[month]["Shopping Spend"]
        outing_spend = actual_expense[month]["Outing Spend"]
        saving_spend = actual_expense[month]["Took From Savings"]

        print("\n===== Financial Summary =====")

        print("Salary:", salary)

        print(f"""
Bill Summary
Budget: {bill_budget}
Spent: {bill_spend}""")

        bill_remaining = bill_budget - bill_spend

        if bill_remaining >= 0:
            print("Remaining:", bill_remaining)

        else:
            print("Exceeded by:", abs(bill_remaining))

        print(f"""
Shopping Summary
Budget: {shopping_budget}
Spent: {shopping_spend}""")

        shopping_remaining = shopping_budget - shopping_spend

        if shopping_remaining >= 0:
            print("Remaining:", shopping_remaining)

        else:
            print("Exceeded by:", abs(shopping_remaining))

        print(f"""
Outing Summary
Budget: {outing_budget}
Spent: {outing_spend}""")

        outing_remaining = outing_budget - outing_spend

        if outing_remaining >= 0:
            print("Remaining:", outing_remaining)

        else:
            print("Exceeded by:", abs(outing_remaining))

        print(f"""
Saving Summary
Budget: {saving_budget}
Taken From Savings: {saving_spend}""")

        saving_remaining = saving_budget - saving_spend

        if saving_remaining >= 0:
            print("Remaining:", saving_remaining)

        else:
            print("Exceeded by:", abs(saving_remaining))

    # fifth condition
    elif choice == 5:

        try:
            asking = int(input("""\nWhich category Summary you want to see?
        1. Bill
        2. Shopping
        3. Outing
        4. Saving
        5. Exit
        Choice: """))

        except ValueError:
            print("Choose number between 1-5")
            continue

        if asking == 1:

            bill_spend = actual_expense[month]["Bill Spend"]

            print(f"""
Bill Summary
Budget: {bill_budget}
Spent: {bill_spend}""")

            bill_remaining = bill_budget - bill_spend

            if bill_remaining >= 0:
                print("Remaining:", bill_remaining)

            else:
                print("Exceeded by:", abs(bill_remaining))

        elif asking == 2:

            shopping_spend = actual_expense[month]["Shopping Spend"]

            print(f"""
Shopping Summary
Budget: {shopping_budget}
Spent: {shopping_spend}""")

            shopping_remaining = shopping_budget - shopping_spend

            if shopping_remaining >= 0:
                print("Remaining:", shopping_remaining)

            else:
                print("Exceeded by:", abs(shopping_remaining))

        elif asking == 3:

            outing_spend = actual_expense[month]["Outing Spend"]

            print(f"""
Outing Summary
Budget: {outing_budget}
Spent: {outing_spend}""")

            outing_remaining = outing_budget - outing_spend

            if outing_remaining >= 0:
                print("Remaining:", outing_remaining)

            else:
                print("Exceeded by:", abs(outing_remaining))

        elif asking == 4:

            saving_spend = actual_expense[month]["Took From Savings"]

            print(f"""
Saving Summary
Budget: {saving_budget}
Taken From Savings: {saving_spend}""")

            saving_remaining = saving_budget - saving_spend

            if saving_remaining >= 0:
                print("Remaining:", saving_remaining)

            else:
                print("Exceeded by:", abs(saving_remaining))

        elif asking == 5:
            print("Returning to main menu...")
            continue

        else:
            print("Choose between 1-5")

    # sixth condition
    elif choice == 6:

        print("Thank you for using Expense Tracker")
        break

    else:

        print("Choose between 1-6")

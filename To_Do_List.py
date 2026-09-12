# TO DO LIST

works = []

while True:
    print("""
What you want to do?
    1. Add work
    2. Remove work
    3. Visit the list
    4. Exit""")
    
    choice = input("Enter the number:\n").strip() 
    
    if choice == "1":
        while True:
            work = input("Enter task:\n").strip()
            if work: # Ensures the user didn't just press enter
                works.append(work)
                print("Task has been added Successfully")
            
            more = input("Do you want to add more? (yes/no):\n").lower().strip()
            if more == "no":
                break
            # If they say "yes", the loop repeats naturally. 
            # If they type anything else, it goes back to the main menu.

    elif choice == "2":
        remove = input("Which work you want to remove?\n").strip()
        # FIX: Use 'in' to check existence directly instead of a broken loop
        if remove in works:
            works.remove(remove)
            print("Task has been removed!")
        else:
            print("This task doesn't exist in your list")

    elif choice == "3":
        if not works:
            print("Your TO DO LIST is empty!")
        else:
            # FIX: Print the header ONCE outside the loop
            print("\n--- Your TO DO LIST ---")
            # Using enumerate to display numbered bullet points (1., 2., etc.)
            for index, item in enumerate(works, start=1):
                print(f"{index}. {item}")

    elif choice == "4":
        print("Bye")
        break
    else:
        print("Invalid Choice! Please enter a number from 1 to 4.")        

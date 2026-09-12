# Create empty contact dictionary
Contact = {}                 

# Start infinite loop
while True:                  
    # Get user menu choice
    choice = int(input("""\nWhat would you like to do:
1. Add contact 
2. Find contact 
3. Exit\n""")) 

    # Choice for adding contact
    if choice == 1: 
        # Get formatted name input
        name = input("Enter your name\n").title().strip() 
        # Get integer phone input
        phone = int(input("Enter your number\n")) 
        # Get cleaned email input
        email = input("Enter your email address\n").strip() 
        
        # Check if completely empty       
        if name == "" and phone == "" and email == "": 
            print("All information are required") 
        # Save contact details
        else: 
            # Store nested contact data
            Contact[name] = { 
                "Phone:": phone, 
                "Email:": email 
            } 
            print("Contact has been successfully added!") 
            
    # Choice for finding contact
    elif choice == 2: 
        # Get formatted search name
        search_name = input("Enter the name you want to find\n").title().strip() 
        
        # Check if contact exists
        if search_name in Contact: 
            print("Contact has been found") 
            print("Name:", search_name) 
            # Print nested phone number
            print("Phone:", Contact[search_name]["Phone:"]) 
            # Print nested email address
            print("Email:", Contact[search_name]["Email:"]) 
        # Handle missing contact
        else: 
            print("Contact not found") 
            
    # Choice for program exit
    elif choice == 3: 
        print("Contact book closed successfully") 
        # Stop the loop
        break 
        
    # Handle invalid menu numbers
    else: 
        print("Invalid choice. Enter from 1, 2, 3")

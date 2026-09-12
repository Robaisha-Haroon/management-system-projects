# Empty dictionary for data
students = {}

# Start infinite program loop
while True:
    # Get user menu choice
    choice = int(input("""What you want to do?
                 1. add record
                 2. find record
                 3. exit\n"""))
                 
    # Choice for adding record
    if choice == 1:
        # Get clean student name
        name = input("Enter your name\n").strip().title()
        # Get user marks input
        marks = int(input("Enter your marks\n"))  
        
        # Validate marks above zero
        if marks <= 0:
            print("Not possible: invalid marks.")
        # Proceed with valid marks
        else:
            # Calculate percentage grade
            score = (marks / 100) * 100
            
            # Check for A grade
            if score >= 80:
                grade = "A"
            # Check for B grade
            elif score >= 70:
                grade = "B"
            # Check for C grade
            elif score >= 60:
                grade = "C"
            # Check for D grade
            elif score >= 50:
                grade = "D"
            # Handle failing grade
            else:
                grade = "F"
                
            # Store nested student data
            students[name] = {
                "Marks": marks,
                "Grade": grade
            }
            print("Record saved successfully!")
        
    # Choice for finding record
    elif choice == 2:
        # Get search student name
        find = input("Enter name\n").strip().title()
        # Check if student exists
        if find in students:
            # Print specific record details
            print("Name:", find)
            print("Marks:", students[find]["Marks"])
            print("Grade:", students[find]["Grade"])
        # Handle missing student record
        else:
            print("record not found")
            
    # Choice for exiting program
    elif choice == 3:
        # Break the loop
        break

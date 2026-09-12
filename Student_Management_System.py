# Student Management system

# empty dictionary
student_record= {}
# infinite loop
while True:
    choice= int(input("""What would you like to do?
                        1. add record
                        2. find record
                        3. exit"""))
    if choice== 1:
        ID= input("Enter ID number:")
        name= input("Enter name:").strip().title()
        age= int(input("Enter age:"))
        course= input("What course?")
        student_record[name]= {
        "ID" : ID,
        "Name" : name,
        "Age" : age,
        "Course" : course}
    elif choice== 2:
        find= input("Enter the name or ID").strip().title()
        for i in student_record.items():
            if find == name or find == ID:
                print(student_record)
            else:
                print("No such name or ID exist")
    elif choice == 3:
        break
    else:
        print("Choose number according to perform task")

# Temperature Converter using functions

def C_answer(f):
    return (f-32)/1.8
def F_answer(c):
    return (1.8*c)+32

choice = int(input("""Enter what you want to do?
            1. celcius to farenhite
            2. farenhite to celcius\n""" ))
if choice == 1:
    num= int(input("Enter number you want to convert in Farenhite\n"))
    print(F_answer(num))
elif choice == 2:
    num= int(input("Enter number you want to convert in Celcius\n"))
    print(C_answer(num))
else:
    print("Invalid Choice. Choose between 1 and 2")

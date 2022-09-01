from random import choice
import operations
program_running = True

while program_running:
    program_option = input("""
Enter options 1 - 4 to select operation;
1 -> Additon
2 -> Subtraction
3 -> Multiplication
4 -> Division

Enter option here: """)

    if program_option == '1':
        print("""READ THIS !!!
* The addition calculator will ask for the number of inputs.
* This will enable it know how many figures you wish to sum.
* Then an input form will be displayed to you depending on the number of inputs specified
* After that all number entered will be added to a single figure.
        """)
        operations.addition()
    elif program_option == '2':
        print("""READ THIS !!!
* The subtraction calculator will ask for the number of inputs.
* This will enable it know how many figures you wish to subtract.
* Then an input form will be displayed to you depending on the number of inputs specified
* After that all number entered will be subtracted to a single figure.
        """)
        operations.subtraction()

    elif program_option == '3':
        print("""READ THIS !!!
* The multiplication calculator will ask for the number of inputs.
* This will enable it know how many figures you wish to subtract.
* Then an input form will be displayed to you depending on the number of inputs specified
* After that all number entered will be multiplied to a single figure.
        """)
        operations.multiplication()

    elif program_option == '4':
        print("""READ THIS !!!
* The multiplication calculator will ask for the number of inputs.
* This will enable it know how many figures you wish to subtract.
* Then an input form will be displayed to you depending on the number of inputs specified
* After that all number entered will be multiplied to a single figure.
        """)
        operations.division()
    else:
        print('Wrong Input!')

    choice_to_continue = input("Do you wish to perform another operation (Y/N) ? \n").lower()
    if choice_to_continue == "y":
        print("Pick another opion from the list")
    elif choice_to_continue == 'n':
        print("Ok 👋 bye See yah later")
        program_running = False
    else:
        while choice_to_continue != 'y' or choice_to_continue == 'n':
            print("Your option should either be (Y/N)")
            choice_to_continue = input("Do you wish to perform another operation (Y/N) ? \n").lower()

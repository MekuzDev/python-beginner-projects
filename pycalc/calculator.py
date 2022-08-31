import operations
program_option = input("""#WELCOME TO PYCALC
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
    * After that all number entered will be sumed to a single figure.
    """)
    operations.addition()
elif program_option == '2':
    print("""READ THIS !!!
    * The addition calculator will ask for the number of inputs.
    * This will enable it know how many figures you wish to subtract.
    * Then an input form will be displayed to you depending on the number of inputs specified
    * After that all number entered will be sumed to a single figure.
    """)
    operations.subtraction()
elif program_option == '3':
    print('Multiplication program Loaded')
elif program_option == '4':
    print('Division program Loaded')
else:
    print("You entered a wrong input")
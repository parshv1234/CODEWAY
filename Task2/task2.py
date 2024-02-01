# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 21:40:38 2024

@author: Parshv
"""

def main():
    print("Simple Calculator")
    print("-------------------")

    while True:
        user_selection = input("Do you wish to use calculator?\nPress 'Y/y' to Continue, or 'N/n' to Exit: ")

        if user_selection.lower() == 'n':
            print("Thank You! See you next time.")
            break
        elif user_selection.lower() == 'y':
            operators = {
                '+': lambda x, y: x + y,
                '-': lambda x, y: x - y,
                '*': lambda x, y: x * y,
                '/': lambda x, y: x / y if y != 0 else None,
                '//': lambda x, y: x // y if y != 0 else None,
                'exp': lambda x, y: x ** y,
                'mod': lambda x, y: x % y if y != 0 else None
            }

            operation = input('''\n********************************************
Please select the operators:
+ for addition (a)
- for subtraction (s)
* for multiplication (m)
/ for division (d)
// for integer division (id)
exp for exponentiation
mod for modulus
********************************************
Enter the operator you want to use: ''')

            if operation in operators:
                n1 = float(input('Enter your first number: '))
                n2 = float(input('Enter your second number: '))

                result = operators[operation](n1, n2)

                if result is not None:
                    print(f"{n1} {operation} {n2} = {result}")
                else:
                    print("Error: Cannot divide by zero.")
            else:
                print('You have not entered a valid operator. Please run the program again.')
            print("")
        else:
            print("Invalid Input! Try Again.")
            print("")

if __name__ == "__main__":
    main()




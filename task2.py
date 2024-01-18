# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 21:40:38 2024

@author: Parshv
"""

def main():
    print("Simple Calculator")
    print("-------------------")

    while True:
        user_selection = input("Do you wish to use calculator ?\nPress 'Y/y' to Continue, or 'N/n' to Exit: ")
        
        if user_selection.lower() == 'n':
            print("Thank You! See you next time.")
            break
        elif user_selection.lower() == 'y':
            operation = input('''\n********************************************
 Please select the operators:
 + for addition (a)
 - for subtraction (s)
 * for multiplication (m)
 / for division (d)
 // for integer division (id)
********************************************
Enter the operator you want to use:''')
                              
            n1=int(input('Enter your first number:'))       
            n2=int(input('Enter your second number:'))       
             
            if operation =='a' or operation =='+':
                print(n1,'+',n2,"=",n1+n2)
                
            elif operation =='-' or operation =='s':
                print(n1,'-',n2,"=",n1-n2)
               
            elif operation =='*' or operation =='m':
                print(n1,'*',n2,"=",n1*n2)
               
            elif operation =='/' or operation =='d':
                print(n1,'/',n2,"=",n1/n2)
               
            elif operation =='//' or operation =='id':
                print(n1,'//',n2,"=",n1//n2)
               
            else:
                print('You have not typed a valid operator, please run the program again.')
                       
            print("")
        else:
            print("Invalid Input! Try Again.")
            print("")

if __name__ == "__main__":
    main()



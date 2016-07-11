# -*- coding: utf-8 -*-
"""
Created on Mon Jul 11 10:25:59 2016

@author: mahmutkilic
"""

start = """
(1) addition
(2) subtraction
(3) multiplication
(4) division
(5) square
(6) square root
"""
print(start)

# Our if, elif and else statement all depends on key = 1, if we change that to something else, it wont't work.
key = 1
while key == 1:
    question = input("Please enter the number for calculation you like to do (To quit type q): ")
    # This is where we set key = 0, so while statement is not true and our program stop working.
    if question == "q":
        print("exiting...")
        key = 0
    # For all calculation we are using build function in Python: + - * / **
    elif question == "1":
        number1 = int(input("For addition enter first number: "))
        number2 = int(input("For addition enter second number: "))
        print(number1, "+", number2, "=", number1 + number2)
    elif question == "2":
        number3 = int(input("For subraction enter first number: "))
        number4 = int(input("For subraction enter second number: "))
        print(number3, "-", number4, "=", number3 - number4)
    elif question == "3":
        number5 = int(input("For multiplication enter first number: "))
        number6 = int(input("For multiplication enter second number: "))
        print(number5, "x", number6, "=", number5 * number6)
    elif question == "4":
        number7 = int(input("For division enter first number: "))
        number8 = int(input("For division enter second number: "))
        print(number7, "/", number8, "=", number7 / number8)
    elif question == "5":
        number9 = int(input("Enter the number you want to calculate the square: "))
        print(number9, "square is =", number9 ** 2)
    elif question == "6":
        number10 = int(input("Enter the number you want to calculate the square root: "))
        print(number10, "square root is = ", number10 ** 0.5)
    else:
        print("Wrong key.")
        print("Enter one of the following options:", start)
key = 1
while key == 1:
    question1 = input("Enter the number you want to do calculation (to quit type  q): ")
    if question == "q":
        print("exiting...")
        key = 0

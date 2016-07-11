# -*- coding: utf-8 -*-
"""
Created on Mon Jul 11 15:41:37 2016

@author: mahmutkilic
"""

allowed_characters = "0123456789+-/*= "
print("""
Basic calculator application.
Operators:
    +   addition
    -   subtraction
    *   multiplication
    /   division
Type the desired operation and press ENTER. 
(Example 23 and 46 to multiple
Type 23 * 46 then press ENTER.)
""")
while True:
    data = input("Please enter your calculation: ")
    if data == "q":
        print("Exiting...")
        break
    for s in data:
        if s not in allowed_characters:
            print("Invalid character!")
            quit()
    calculate = eval(data)
    print(calculate)

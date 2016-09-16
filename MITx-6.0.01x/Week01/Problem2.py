"""
Assume s is a string of lower case characters.
Write a program that prints the number of times the string 'bob' occurs in s. For example, if s = 'azcbobobegghakl', then your program should print
Number of times bob occurs is: 2
"""

count = 0
for x in range(len(s)):
    if s[x:x+3] == 'bob':
        count += 1
print(count) 

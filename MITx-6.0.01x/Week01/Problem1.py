"""
Assume s is a string of lower case characters.
Write a program that counts up the number of vowels contained in the string s. Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example, if s = 'azcbobobegghakl', your program should print:
Number of vowels: 5
"""


count = 0
vowels = 'aeiou'
for word in s:
    if word in vowels:
        count += 1
print(count)

#we store the name of the file we’re reading from in the variable filename
filename = '/Users/mahmutkilic/Desktop/pi_million_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()

#we create a variable, pi_string, to hold the digits of pi.
pi_string = ''
for line in lines:
    pi_string += line.rstrip()

birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi.")
else:
    print("Your birthday does not appear in the first million digits of pi.")


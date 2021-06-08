import re

#Open the File
fhand = open('regex_sum_1228869.txt')
numbers = list()

#read the lines in the file
for line in fhand:
    # Strip the line to search for numbers
    line = line.strip()
    digits = re.findall('[0-9]+', line)
    # if the lenght of digits is 0 then Continue
    #Cause the line doesn´t have numbers
    if len(digits) < 1:
        continue
    # Take the numbers in the line, cast them into
    #integers and append them in the list
    else:
        for digit in digits:
            digit = int(digit)
            numbers.append(digit)

#print the sum of the  numbers in the list
print(sum(numbers))


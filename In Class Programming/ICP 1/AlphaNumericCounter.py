print('This program takes a sentance and returns the number of letters and number contained within it.')
inputString = input("Input a sentence to be counted: ")
#
alphaCount = 0
digitCount = 0
# For loop that checks each character in the string and checks if it is a alpha or digit
for char in inputString:
    if char.isalpha():
        alphaCount += 1
    elif char.isdigit():
        digitCount += 1
# Print results
print('Letters:' + str(alphaCount) + "  Digits:" + str(digitCount))
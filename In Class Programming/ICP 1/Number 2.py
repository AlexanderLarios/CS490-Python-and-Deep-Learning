# user input
firstName = input('Please enter your first name')
lastName = input('Please enter your last name')

firstNumberString = input('Please enter your favorite integer')
secondNumberString = input('Please enter your second favorite integer')

firstNum = int(firstNumberString)
secondNum = int(secondNumberString)

# reverse the names
reverseFName = ''.join(reversed(firstName))
reverseLName = ''.join(reversed(lastName))

# perform arithmetic operations
add = firstNum + secondNum
multiply = firstNum * secondNum
divide = firstNum/secondNum

# print the manipulated values
print('Reversed first name: ' + reverseFName + ' Reversed last name: ' + reverseLName)
print('The numbers multiplied is: ' + str(multiply) + ' The numbers added is: ' + str(add) + ' The numbers divided is: '
      + str(divide))

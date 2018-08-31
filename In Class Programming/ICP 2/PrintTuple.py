userNumbers = input("Enter desired numbers.  Seperate with ' ': ")
listNumbers = [int(i) for i in userNumbers.split()]
listLength = len(listNumbers)
tupleNumber = (listNumbers[0], listNumbers[listLength -1])
print(tupleNumber)
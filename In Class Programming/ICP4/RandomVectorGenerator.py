import numpy
# Generate random array range 0-20 and size 15
random_array = numpy.random.randint(0, 20, 15)
#find most frequent element
freqElement = numpy.bincount(random_array).argmax()
#Print to console
print("Here is the random array: " + str(random_array))
print("The most common element is: " + str(freqElement))
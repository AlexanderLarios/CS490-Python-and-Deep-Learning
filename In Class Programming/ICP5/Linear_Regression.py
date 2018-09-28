import numpy as numpy
import matplotlib.pyplot as plyplot
import csv

x_value = []
y_value = []

# read in x and y values
with open('slr04.csv') as csvfile:
    csvData = csv.reader(csvfile, delimiter=',')
    next(csvData, None)
    for row in csvData:
        x_value.append(float(row[0]))
        y_value.append(float(row[1]))

# find x and y mean values
x_mean = numpy.mean(x_value)
y_mean = numpy.mean(y_value)

total_values = len(x_value)

# calculate necessary pieces to find b1 / b0
num = 0
denom = 0
for i in range(total_values):
    num += (x_value[i] - x_mean) * (y_value[i] - y_mean)
    denom += (x_value[i] - x_mean) ** 2

# calculate b1 and b0
b1 = num / denom
b0 = y_mean - (b1 * x_mean)

# create y = mx + b line for plotting
x = numpy.linspace(1, 12, 100)
y = b0 + b1 * x

# plot the graph and make it pretty
plyplot.plot(x, y, '-g')
plyplot.scatter(x_value, y_value, c='r')
plyplot.grid()
plyplot.xlabel('X Values')
plyplot.ylabel('Y Values')
plyplot.suptitle('Linear Regression')
plyplot.show()

from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

iris_dataset = datasets.load_iris()
x=iris_dataset.data
y = iris_dataset.target

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

# Guassian Naive Bayes
gnb = GaussianNB()

# fit the model
gnb.fit(x_train, y_train)

# predict the values
prediction = gnb.predict(x_test)
print(prediction)

# print the numbers
print("Nubmer of mislabeled points out of " + str(x_test.shape[0]) + " points : " + str((y_test != prediction).sum()))

# find and format the accuracy
accuracy = accuracy_score(y_test, prediction, normalize=True)
rounded = round(accuracy, 2)
print("Accuracy = " + str(rounded))



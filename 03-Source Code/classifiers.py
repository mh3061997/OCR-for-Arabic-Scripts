from sklearn.svm import SVC
from commonfunctions import *

def read_data(filename):
    data = []
    # TODO 1 : Read the file 'data1.csv' into the variable data.
    f = open(filename, "r")
    for line in f:
        data.append(line.split(','))

    for i in range(len(data)):
        for j in range(len(data[0])):
            data[i][j] = float(data[i][j])

    # print(data[0][0])
    # data contains the training data together with labelled classes.
    return data

def SVM_linear_Classifier(X_train,y_train,X_test): # X_train is the training features , y_train is the training labels , X_test is the test features
    svm_model_linear = SVC(kernel = 'linear', C = 1).fit(X_train, y_train)
    svm_predictions = svm_model_linear.predict(X_test)
    return svm_predictions

def SVM_Non_linear_Classifier(X_train,y_train,X_test): # X_train is the training features , y_train is the training labels , X_test is the test features
    svclassifier = SVC(kernel='poly', degree=8)
    svclassifier.fit(X_train, y_train)
    svm_predictions = svclassifier.predict(X_test)
    return svm_predictions



#X1=numpy.matrix([[1, 2,3], [3, 4,6]])
#y1=[0,1]
#X2=numpy.matrix([[7,0,1],[3,4,6]])
#y2=SVM_linear_Classifier(X1,y1,X2)
#y3=SVM_Non_linear_Classifier(X1,y1,X2)
#print(y2)
#print(y3)
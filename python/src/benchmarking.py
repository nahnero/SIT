# Started Wed 15 Jan 20:33:29 2020 by nahnero. #
"""
Measures times to load and partition, then compares lda, qda and knn.
"""
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis as QDA
from sklearn.neighbors import KNeighborsClassifier
from pythonbenchmark import measure, compare

import pytest

# Absolute times
@measure
def loa ():
    global x_no, y_no
    from preprocessing import x_no, y_no

@measure
def par ():
    global X_train, X_test, y_train, y_test
    X_train, X_test, y_train, y_test = train_test_split (x_no, y_no)

@measure
def lda ():
    lda = LDA ()
    lda.fit (X_train, y_train)
    error = np.sum (abs (lda.predict (X_test) - y_test)) / len (y_test)

@measure
def qda ():
    qda = QDA ()
    qda.fit (X_train, y_train)
    error = np.sum (abs (qda.predict (X_test) - y_test)) / len (y_test)

@measure
def knn ():
    knn = KNeighborsClassifier (n_neighbors = 1)
    knn.fit (X_train, y_train)
    error = np.sum (abs (knn.predict (X_test) - y_test)) / len (y_test)

loa (), par (), lda (), qda (), lda ()

# Relative times
def lda ():
    lda = LDA ()
    lda.fit (X_train, y_train)
    error = np.sum (abs (lda.predict (X_test) - y_test)) / len (y_test)

def qda ():
    qda = QDA ()
    qda.fit (X_train, y_train)
    error = np.sum (abs (qda.predict (X_test) - y_test)) / len (y_test)

def knn ():
    knn = KNeighborsClassifier (n_neighbors = 1)
    knn.fit (X_train, y_train)
    error = np.sum (abs (knn.predict (X_test) - y_test)) / len (y_test)

compare (lda, qda, 1000)
compare (qda, knn, 1000)
compare (lda, knn, 1000)

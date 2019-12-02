# Started Sun  1 Dec 21:59:45 2019 by nahnero. #

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from preprocessing import  x_no, y_no, labels

#  PCA
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

x_no = StandardScaler ().fit_transform (x_no) #  typify

from sklearn.model_selection import train_test_split
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA

pca = PCA (n_components = 5)
x = pca.fit_transform(x_no)
y = y_no

iteraciones = 1000
error =  [None]*iteraciones

for i in range (0, iteraciones):
    X_train, X_test, y_train, y_test = train_test_split (x, y, test_size = 0.3)
    lda = LDA ()
    lda.fit (X_train, y_train)
    error[i] = np.sum (abs (lda.predict (X_test) - y_test))/ len (y_test)


import pandas as pd

pd = pd.DataFrame (error)
print ('Linear error', pd.describe (pd))

from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis as QDA

iteraciones = 1000
error =  [None]*iteraciones

for i in range (0, iteraciones):
    X_train, X_test, y_train, y_test = train_test_split (x, y, test_size = 0.3)
    qda = QDA ()
    qda.fit (X_train, y_train)
    error[i] = np.sum (abs (qda.predict (X_test) - y_test))/ len (y_test)


import pandas as pd

pd = pd.DataFrame (error)
print ('Quadratic error:', pd.describe (pd))

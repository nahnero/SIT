# Started Mon  2 Dec 01:24:50 2019 by nahnero. #
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from preprocessing import x_no, y_no, labels

#  PCA
from sklearn.decomposition import PCA
pca = PCA (n_components = 5)
x = pca.fit_transform(x_no)
y = y_no

from sklearn.model_selection import cross_val_score, KFold, ShuffleSplit, LeaveOneOut
from sklearn.neighbors import KNeighborsClassifier

knn = KNeighborsClassifier (n_neighbors = 9)
error = cross_val_score (knn, x, y, cv = 10)
print ('KNN puntuación CV media: %.2f std: %.2f'
        %(np.mean (error), np.std (error)))

error = cross_val_score (knn, x, y, cv = KFold (n_splits = 10, shuffle = True))
print ('KNN puntuación KF media: %.2f std: %.2f'
        %(np.mean (error), np.std (error)))

error = cross_val_score (knn, x, y, cv = ShuffleSplit (n_splits = 10))
print ('KNN puntuación SS media: %.2f std: %.2f'
        %(np.mean (error), np.std (error)))

error = cross_val_score (knn, x, y, cv = LeaveOneOut ())
print ('KNN puntuación LO media: %.2f std: %.2f'
        %(np.mean (error), np.std (error)))

from sklearn.model_selection import train_test_split

vecinos = 70
score = [None]*(vecinos)
for i in range (2,vecinos):
    print ('n_neighbors = %i'% (i), end = '\r')
    iteraciones = 1000
    error =  [None]*iteraciones
    for j in range (0, iteraciones):
        X_train, X_test, y_train, y_test = train_test_split (x, y, test_size = 0.3)
        knn = KNeighborsClassifier (n_neighbors = i)
        knn.fit (X_train, y_train)
        error[j] = np.sum (abs (knn.predict (X_test) - y_test))/ len (y_test)
    score[i] = np.mean (error)

plt.plot (range (2, vecinos+2), score)

plt.suptitle ('Puntuación vs. Vecinos', fontsize = 10)
plt.xlabel ('Vecinos')
plt.ylabel ('Puntuación')
plt.savefig  ('../images/knn.pdf', bbox_inches = 'tight', pad_inches = 0)

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

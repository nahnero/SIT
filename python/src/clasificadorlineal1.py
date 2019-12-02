# Started Sun  1 Dec 21:59:45 2019 by nahnero. #
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from preprocessing import  x_no, y_no, labels

#  PCA
from sklearn.decomposition import PCA
pca = PCA (n_components = 5)
x = pca.fit_transform(x_no)
y = y_no

from sklearn.model_selection import cross_val_score, KFold, ShuffleSplit, LeaveOneOut
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA

lda = LDA ()
error = 1 - cross_val_score (lda, x, y, cv = 10)
print ('Linear error CV media: %.2f std: %.2f'
        %(np.mean (error), np.std (error)))

error = 1 - cross_val_score (lda, x, y, cv = KFold (n_splits = 10, shuffle = True))
print ('Linear error KF media: %.2f std: %.2f'
        %(np.mean (error), np.std (error)))

error = 1 - cross_val_score (lda, x, y, cv = ShuffleSplit (n_splits = 10))
print ('Linear error SS media: %.2f std: %.2f'
        %(np.mean (error), np.std (error)))

error = 1 - cross_val_score (lda, x, y, cv = LeaveOneOut ())
print ('Linear error LO media: %.2f std: %.2f'
        %(np.mean (error), np.std (error)))

print ()

from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis as QDA

qda = QDA ()
error = 1 - cross_val_score (qda, x, y, cv = 10)
print ('Quadratic error CV media: %.2f std: %.2f'
        %(np.mean (error), np.std (error)))

error = 1 - cross_val_score (qda, x, y, cv = KFold (n_splits = 10, shuffle = True))
print ('Quadratic error KF media: %.2f std: %.2f'
        %(np.mean (error), np.std (error)))

error = 1 - cross_val_score (qda, x, y, cv = ShuffleSplit (n_splits = 10))
print ('Quadratic error SS media: %.2f std: %.2f'
        %(np.mean (error), np.std (error)))

error =  (1 - cross_val_score (qda, x, y, cv = LeaveOneOut ()))
print ('Quadratic error LO media: %.2f std: %.2f'
        %(np.mean (error), np.std (error)))


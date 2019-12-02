# Started Sun  1 Dec 21:59:45 2019 by nahnero. #
"""
Trains an LDA & QDA model and validates using automatic methods (Cross
Validation, K Folds, Shuffle Split and Leave One Out).
"""
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
score = cross_val_score (lda, x, y, cv = 10)
print ('Linear puntuación CV media: %.2f std: %.2f'
        %(np.mean (score), np.std (score)))

score = cross_val_score (lda, x, y, cv = KFold (n_splits = 10, shuffle = True))
print ('Linear puntuación KF media: %.2f std: %.2f'
        %(np.mean (score), np.std (score)))

score = cross_val_score (lda, x, y, cv = ShuffleSplit (n_splits = 10))
print ('Linear puntuación SS media: %.2f std: %.2f'
        %(np.mean (score), np.std (score)))

score = cross_val_score (lda, x, y, cv = LeaveOneOut ())
print ('Linear puntuación LO media: %.2f std: %.2f'
        %(np.mean (score), np.std (score)))

print ()

from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis as QDA

qda = QDA ()
score = cross_val_score (qda, x, y, cv = 10)
print ('Quadratic puntuación CV media: %.2f std: %.2f'
        %(np.mean (score), np.std (score)))

score = cross_val_score (qda, x, y, cv = KFold (n_splits = 10, shuffle = True))
print ('Quadratic puntuación KF media: %.2f std: %.2f'
        %(np.mean (score), np.std (score)))

score = cross_val_score (qda, x, y, cv = ShuffleSplit (n_splits = 10))
print ('Quadratic puntuación SS media: %.2f std: %.2f'
        %(np.mean (score), np.std (score)))

score = cross_val_score (qda, x, y, cv = LeaveOneOut ())
print ('Quadratic puntuación LO media: %.2f std: %.2f'
        %(np.mean (score), np.std (score)))


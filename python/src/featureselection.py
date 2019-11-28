#!/usr/bin/env python3.7
import sys
sys.path.append ('/usr/local/lib/python3.7/site-packages/')

# Started Tue 26 Nov 11:04:07 2019 by nahnero. #
"""
This script imports matrix x and vector y and selects fetures
according to different method
"""

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from preprocessing import  x_no, y_no, labels

#  Filter Methods
import sklearn.feature_selection as sk

Fscore, pval = sk.f_classif (x_no, y_no)
r1 = Fscore.argsort().argsort() #  fscore rank
print (r1+1)

import ReliefF as rl

r2 = rl.ReliefF (n_neighbors = 1) #  relieff rank
r2.fit(x_no, y_no)
r2 = r2.top_features
print (r2+1)

diferencias = abs (r1-r2)
media = np.mean (diferencias)

print (diferencias)
print (media, end = '\n\n')

#  Wrapper Methods
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsClassifier
from mlxtend.feature_selection import SequentialFeatureSelector

knn = KNeighborsClassifier (n_neighbors = 50)

sfs = SequentialFeatureSelector (knn,
                k_features = 4,
                forward = True,
                scoring = 'accuracy',
                cv = 10)

sfs.fit (x_no, y_no, custom_feature_names = labels)
print (sfs.k_score_)
print ('Sequential Forward  Selection', sfs.k_feature_names_, end = '\n\n')

sfs.forward = False

sfs.fit (x_no, y_no, custom_feature_names = labels)
print (sfs.k_score_)
print ('Sequential Backward Selection', sfs.k_feature_names_, end = '\n\n')

#  PCA
from sklearn.preprocessing import StandardScaler
x_no = StandardScaler ().fit_transform (x_no) #  typify

from sklearn.decomposition import PCA
pca = PCA (n_components = 9)
principalComponents = pca.fit_transform(x_no)
evr = pca.explained_variance_ratio_

print (evr)
print (np.cumsum (evr))

#  Pareto
fig, ax = plt.subplots ()
ax.bar (range (len (evr)), evr)
ax.set_ylim (top=1)

ax1 = ax.twinx ()
ax1.set_ylim (top=100)
ax1.plot (range (len (evr)), np.cumsum (evr)*100, marker = '.', color = 'red')

fig.suptitle ('Pareto', fontsize = 20)
fig.savefig  ('../images/pareto.pdf', bbox_inches = 'tight', pad_inches = 0)

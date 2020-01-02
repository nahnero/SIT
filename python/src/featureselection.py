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

#  Biplot
def biplot (score,coeff,labels=None):
    """from https://ostwalprasad.github.io/machine-learning/PCA-using-python.html"""
    xs = score[:,0]; ys = score[:,1]
    n = coeff.shape[0]
    scalex = 1.0/(xs.max() - xs.min())
    scaley = 1.0/(ys.max() - ys.min())
    plt.scatter(xs * scalex,ys * scaley,s=5)
    plt.suptitle ('Biplot Python', fontsize = 16)
    for i in range(n):
        plt.arrow(0, 0, coeff[i,0], coeff[i,1],color='r',alpha=0.5, head_width=0.01)
        if labels is None:
            plt.text(coeff[i,0]* 1.15, coeff[i,1] * 1.15, "Var"+str(i+1), color = 'green', ha = 'center', va = 'center')
        else:
            plt.text(coeff[i,0]* 1.15, coeff[i,1] * 1.15, labels[i], color = 'g', ha = 'center', va = 'center')
    plt.xlabel("PC{}".format(1)), plt.ylabel("PC{}".format(2))
    plt.savefig  ('../images/biplotpca.pdf', bbox_inches = 'tight', pad_inches = 0)
biplot (principalComponents[:,0:2], np.transpose(pca.components_[0:2, :]), labels)



#  Pareto
fig, ax = plt.subplots ()
ax.bar (range (len (evr)), evr)
ax.set_ylim (top=1)
ax1 = ax.twinx ()
ax1.set_ylim (top=100)
ax1.plot (range (len (evr)), np.cumsum (evr)*100, marker = '.', color = 'red')
fig.suptitle ('Pareto Python', fontsize = 16)
fig.savefig  ('../images/pareto.pdf', bbox_inches = 'tight', pad_inches = 0)

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
import ReliefF as rl
import sklearn.feature_selection as sk
from preprocessing import  x_no, y_no, labels


Fscore, pval = sk.f_classif (x_no, y_no)
r1 = Fscore.argsort().argsort() #  fscore rank

print (r1+1)

r2 = rl.ReliefF (n_neighbors = 1) #  relieff rank
r2.fit(x_no, y_no)
r2 = r2.top_features

print (r2+1)

diferencias = abs (r1-r2)
print (diferencias)
print (np.mean (diferencias))

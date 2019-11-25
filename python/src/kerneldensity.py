# Started Mon 25 Nov 13:46:08 2019 by nahnero. #
"""
This script imports matrix x and vector y and generates kernel density plots,
'../images/kden.pdf' contains the plots before removing outliers. Then it
imports from the preprocessing module x_no and y_no, the same data without the
outliers. It generates the plots '../images/kden1.pdf'.
"""

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import gaussian_kde

#  load preprocessed data, x and y are raw, x_no and y_no contain no outliers
from preprocessing import x, y, x_no, y_no, labels

#  colours
fc = ['', 'green', 'blue']

fig, ax = plt.subplots (nrows = 5, ncols = 2, figsize = (13, 10))
ax = ax.flatten ()

#  same loop in principle as before
for i in range (0, 9):
    for j in [1, 2]:
        kde = gaussian_kde (x_ := x [y == j, i])
        xs = np.linspace(np.min (x_) - 10, np.max (x_), num=len (x_))
        ax[i].plot (xs, kde(xs), c = fc[j], label = labels [i] + str (j))
        ax[i].legend (loc = 1, prop={'size': 15})

fig.suptitle ('con anómalos', fontsize = 30)
fig.savefig  ('../images/kden.pdf', bbox_inches = 'tight', pad_inches = 0)

###############################
#  SAME BUT WITHOUT OUTLIERS  #
###############################

fig_no, ax_no = plt.subplots (nrows = 5, ncols = 2, figsize = (13, 10))
ax_no = ax_no.flatten ()

for i in range (0, 9):
    for j in [1, 2]:
        kde = gaussian_kde (x_ := x_no [y_no == j, i])
        xs = np.linspace(np.min (x_) - 10, np.max (x_), num=len (x_))
        ax_no[i].plot (xs, kde(xs),c = fc[j], label = labels [i] + str (j))
        ax_no[i].legend (loc = 1, prop={'size': 15})

fig_no.suptitle ('sin anómalos', fontsize = 30)
fig_no.savefig  ('../images/kden1.pdf', bbox_inches = 'tight', pad_inches = 0)

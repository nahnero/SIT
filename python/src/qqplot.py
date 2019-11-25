# Started Mon 25 Nov 22:39:19 2019 by nahnero. #
"""
This script imports matrix x and vector y and generates qq plots,
'../images/qqp.pdf' contains the plots before removing outliers. Then it
imports from the preprocessing module x_no and y_no, the same data without the
outliers. It generates the plots '../images/qqp1.pdf'.
"""

import matplotlib as mpl
import matplotlib.pyplot as plt

#  load preprocessed data, x and y are raw, x_no and y_no contain no outliers
from preprocessing import x, y, x_no, y_no, labels
import statsmodels.api as sm

fc = [(), (0, 1, 0, 0.6), (0, 0, 1, 0.6)]

fig, ax = plt.subplots (nrows = 5, ncols = 2, figsize = (13, 10))
ax = ax.flatten ()

for i in range (0, 9):
    for j in [1, 2]:
        sm.qqplot (x [y == j, i], ax = ax[i], c = fc[j],
                line = 's', label = labels [i] + str (j))
        ax[i].legend (loc = 2, prop={'size': 15})

fig.suptitle ('con anómalos', fontsize = 30)
fig.savefig  ('../images/qqp.pdf', bbox_inches = 'tight', pad_inches = 0)

###############################
#  SAME BUT WITHOUT OUTLIERS  #
###############################

fig_no, ax_no = plt.subplots (nrows = 5, ncols = 2, figsize = (13, 10))
ax_no = ax_no.flatten ()

for i in range (0, 9):
    for j in [1, 2]:
        sm.qqplot (x_no [y_no == j, i], ax = ax_no[i], c = fc[j],
                line = 's', label = labels [i] + str (j))
        ax_no[i].legend (loc = 2, prop={'size': 15})

fig_no.suptitle ('sin anómalos', fontsize = 30)
fig_no.savefig  ('../images/qqp1.pdf', bbox_inches = 'tight', pad_inches = 0)

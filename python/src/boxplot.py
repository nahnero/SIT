# Started Mon 25 Nov 20:01:42 2019 by nahnero. #
"""
This script imports matrix x and vector y and generates box plots,
'../images/boxp.pdf' contains the plots before removing outliers. Then it
imports from the preprocessing module x_no and y_no, the same data without the
outliers. It generates the plots '../images/boxp1.pdf'.
"""

import matplotlib as mpl
import matplotlib.pyplot as plt

#  load preprocessed data, x and y are raw, x_no and y_no contain no outliers
from preprocessing import x, y, x_no, y_no, labels

fig, ax = plt.subplots (nrows = 5, ncols = 2, figsize = (13, 10))
ax = ax.flatten ()

for i in range (0, 9):
    ax[i].boxplot ([x [y == 1, i], x [y == 2, i]])
    ax[i].title.set_text (labels [i])

fig.suptitle ('con anómalos', fontsize = 30)
fig.savefig  ('../images/boxp.pdf', bbox_inches = 'tight', pad_inches = 0)

###############################
#  SAME BUT WITHOUT OUTLIERS  #
###############################

fig_no, ax_no = plt.subplots (nrows = 5, ncols = 2, figsize = (13, 10))
ax_no = ax_no.flatten ()

for i in range (0, 9):
    ax_no[i].boxplot ([x_no [y_no == 1, i], x_no [y_no == 2, i]], 0, '')
    ax_no[i].title.set_text (labels [i])

fig_no.suptitle ('sin anómalos', fontsize = 30)
fig_no.savefig  ('../images/boxp1.pdf', bbox_inches = 'tight', pad_inches = 0)

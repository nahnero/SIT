# Started Tue  5 Nov 22:04:06 2019 by nahnero. #
"""
This script imports matrix x and vector y and generates histograms,
'../images/hist.pdf' contains the histograms before removing outliers.
Then it imports from the preprocessing module x_no and y_no, the same
data without the outliers.  It generates the histograms '../images/hist1.pdf'.
"""

import matplotlib as mpl
import matplotlib.pyplot as plt

#  load preprocessed data, x and y are raw, x_no and y_no contain no outliers
from preprocessing import x, y, x_no, y_no, labels

#  colours for the histograms
fc = [(), (0, 1, 0, 0.6), (0, 0, 1, 0.6)]
#         (R, G, B,  $\color[HTML]{228B22}\alpha$  )$\color[HTML]{228B22}\leftarrow$ transparency

fig, ax = plt.subplots (nrows = 5, ncols = 2, figsize = (13, 10))
ax = ax.flatten ()

#  draws each of the histograms, two for each variable
for i in range (0, 9):
    for j in [1, 2]:
        ax[i].hist (x [y == j, i], bins = 15, fc = fc [j], label = labels [i] + str (j))
        ax[i].legend (loc = 1, prop={'size': 15})

fig.suptitle ('con anómalos', fontsize = 30)
fig.savefig  ('../images/hist.pdf', bbox_inches = 'tight', pad_inches = 0)

###############################
#  SAME BUT WITHOUT OUTLIERS  #
###############################

fig_no, ax_no = plt.subplots (nrows = 5, ncols = 2, figsize = (13, 10))
ax_no = ax_no.flatten ()

#  faster, less readable way of coding the loop, they both do exactly SAME thing
[(ax_no[i].hist (x_no [y_no == j, i], bins = 15, fc = fc [j], label = labels [i] + str (j)),
  ax_no[i].legend (loc = 1, prop={'size': 15})) for i in range (0, 9) for j in range (1,3)]

fig_no.suptitle ('sin anómalos', fontsize = 30)
fig_no.savefig  ('../images/hist1.pdf', bbox_inches = 'tight', pad_inches = 0)

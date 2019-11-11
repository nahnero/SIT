# Started Tue  5 Nov 22:04:06 2019 by nahnero. #
"""
This script reads data from ./data.csv, parses class and parameters,
and generates two pdfs, './hist.pdf' containing the histograms before
removing outliers and './hist1.pdf' after.

YOU MUST INSTALL DEPENDENCIES BEFORE RUNNING
    - numpy
    - matplotlib
    - scipy
"""

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from   scipy import stats

#  loads data
data = np.loadtxt (open (r'../../data.csv', 'rb'), delimiter = ',')

#  rewrites $\color[HTML]{000000}\text{data}$ as all the rows of $\color[HTML]{000000}\text{data}$ w/out nan cells
data = data [~np.isnan (data).any (axis=1)]

#  separates parameters into matrix $\color[HTML]{000000}\text{x}$
x    = np.array ([list (data [x][:-1])    for x in range (len (data))])

#  and class (1, 2) into vector $\color[HTML]{000000}\text{y}$
y    = np.array ([int  (data [x][ -1])    for x in range (len (data))])

labels = ['age', 'leptin', 'bmi', 'adiponectin', 'glucose',
        'resistin', 'insulin', 'MCP1', 'HOMA']

#  colours
fc = [(), (0, 1, 0, 0.6), (0, 0, 1, 0.6)]
#         (R, G, B,  $\color[HTML]{228B22}\alpha$  )$\color[HTML]{228B22}\leftarrow$ transparency

fig, ax = plt.subplots (nrows = 5, ncols = 2, figsize = (13, 10))
ax = ax.flatten ()

#  proper, clear way of coding the loop
#  for i in range (0, 9):
    #  for j in [1, 2]:
        #  ax[i].hist (x [y == j, i], bins = 15, fc = fc [j], label = labels [i] + str (j))
        #  ax[i].legend ()

#  faster, less readable way of coding the loop, they both do the SAME thing
[(ax[i].hist (x [y == j, i], bins = 15, fc = fc [j], label = labels [i] + str (j)),
  ax[i].legend ()) for i in range (0, 9) for j in range (1,3)]

fig.suptitle ('con anómalos')
fig.savefig  ('../images/hist.pdf')

###############################
#  SAME BUT WITHOUT OUTLIERS  #
###############################

#  removes outliers
data_no = data [(np.abs (stats.zscore (data)) < 3).all (axis = 1)]
#    $\color[HTML]{228B22}\uparrow$ = No Outliers

x_no = np.array ([list (data_no [x][:-1]) for x in range (len (data_no))])
y_no = np.array ([int  (data_no [x][ -1]) for x in range (len (data_no))])

fig_no, ax_no = plt.subplots (nrows = 5, ncols = 2, figsize = (13, 10))
ax_no = ax_no.flatten ()

[(ax_no[i].hist (x_no [y_no == j, i], bins = 15, fc = fc [j], label = labels [i] + str (j)),
  ax_no[i].legend ()) for i in range (0, 9) for j in range (1,3)]

fig_no.suptitle ('sin anómalos')
fig_no.savefig  ('../images/hist1.pdf')

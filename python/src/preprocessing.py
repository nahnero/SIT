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
from   scipy import stats

#  names of variables
labels = ['age', 'leptin', 'bmi', 'adiponectin', 'glucose',
        'resistin', 'insulin', 'MCP1', 'HOMA']

#  loads data
data = np.loadtxt (open (r'../../data.csv', 'rb'), delimiter = ',')

#  rewrites $\color[HTML]{000000}\text{data}$ as all the rows of $\color[HTML]{000000}\text{data}$ w/out nan cells
data = data [~np.isnan (data).any (axis=1)]

#  separates parameters into matrix $\color[HTML]{000000}\text{x}$
x    = np.array ([list (data [x][:-1])    for x in range (len (data))])

#  and class (1, 2) into vector $\color[HTML]{000000}\text{y}$
y    = np.array ([int  (data [x][ -1])    for x in range (len (data))])

#  removes outliers
data_no = data [(np.abs (stats.zscore (data)) < 3).all (axis = 1)]
#    $\color[HTML]{228B22}\uparrow$ = No Outliers

x_no = np.array ([list (data_no [x][:-1]) for x in range (len (data_no))])
y_no = np.array ([int  (data_no [x][ -1]) for x in range (len (data_no))])

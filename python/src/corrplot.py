# Started Mon 25 Nov 23:10:40 2019 by nahnero. #
"""
This script imports matrix x and vector y and generates qq plots,
'../images/qqp.pdf' contains the plots before removing outliers. Then it
imports from the preprocessing module x_no and y_no, the same data without the
outliers. It generates the plots '../images/qqp1.pdf'.
"""

import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from preprocessing import x, y, x_no, y_no, labels

dataframe = pd.DataFrame.from_records(x)
sns.pairplot(dataframe, kind = 'reg')
plt.suptitle ('con anómalos', fontsize = 30)
plt.savefig  ('../images/corrp.pdf', bbox_inches = 'tight', pad_inches = 0)

###############################
#  SAME BUT WITHOUT OUTLIERS  #
###############################

dataframe = pd.DataFrame.from_records(x_no)
sns.pairplot(dataframe, kind = 'reg')

plt.suptitle ('sin anómalos', fontsize = 30)
plt.savefig  ('../images/corrp1.pdf', bbox_inches = 'tight', pad_inches = 0)


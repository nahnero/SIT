# Started Mon 30 Dec 16:28:26 2019 by nahnero. #
# load data
datos <- read.table ('../../data.csv', sep = ',', header = T)
datos <- na.omit (datos)

# FILTER METHODS
# Fscore
library (PredPsych)
rank (fscore (datos, 10, 1:9))

# Relieff
library (CORElearn)
rank (attrEval (as.factor (clase)~., datos, 'Relief'))

for (i in infoCore (what = "attrEval")){
	cat (i, '\r\t\t',
	     unname (rank (attrEval (as.factor (clase)~., datos, i)))
	     ,'\n')
}

# WRAPPER METHODS
# install.packages ("Boruta")
library (Boruta)
Boruta (as.factor (clase)~., datos, maxRuns = 101) -> borutaout

pdf ("../images/boruta.pdf")
par (mar = c(7,4,4,3))
plot (borutaout, las = 2, xlab = '', main = 'Boruta Variable Importance')
dev.off ()

# Sequential Feature Selector
library (mlr)
# Forward
sfs <- selectFeatures (
      learner    = makeLearner ('classif.knn', k = 9, l = 3),
      task       = makeClassifTask (data = datos, target = 'clase'),
      resampling = makeResampleDesc ("CV", iter = 50),
      control    = makeFeatSelControlSequential (method = "sfs", maxit = 100L))

# Backward
sbs <- selectFeatures (
      learner    = makeLearner ('classif.knn', k = 9, l = 3),
      task       = makeClassifTask (data = datos, target = 'clase'),
      resampling = makeResampleDesc ("CV", iter = 50),
      control    = makeFeatSelControlSequential (method = "sbs", maxit = 100L))

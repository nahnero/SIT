# Started Mon 30 Dec 16:28:26 2019 by nahnero. #

# load data
datos <- read.table ('../../data.csv', sep = ',', header = T)
datos <- na.omit (datos)

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



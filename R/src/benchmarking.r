# Started Thu  2 Jan 21:39:09 2020 by nahnero. #

suppressPackageStartupMessages (library (dplyr))
suppressPackageStartupMessages (library (tidyverse))
suppressPackageStartupMessages (library (caret))
suppressPackageStartupMessages (library (MASS))
suppressPackageStartupMessages (library (class))
suppressPackageStartupMessages (library (rbenchmark))

benchmark (
'1 load'= {
	datos <- read.table ('../../data.csv', sep = ',', header = T)
	datos <- na.omit (datos)
	datos <- filter_all (datos, all_vars (. <= quantile (., 0.99, na.rm = T)))
	p <- 0.7
},
'2 part'= {
	train.samples <- createDataPartition (datos$clase, p = p, list = F)
	train.data    <- datos[ train.samples,]
	test.data     <- datos[-train.samples,]
	preproc.param <- preProcess (train.data, method = c ("center", "scale"))
	train.trans   <- predict (preproc.param, train.data)
	test.trans    <- predict (preproc.param, test.data)
},
'3 lda' = {
	mdl <- lda (clase~., data = train.trans)
	prd <- predict (mdl, test.trans)
	mean (prd$class == test.trans$clase)
},
'4 qda' = {
	mdl <- qda (clase~., data = train.trans)
	prd <- predict (mdl, test.trans)
	mean (prd$class == test.trans$clase)
},
'5 knn' = {
	prd <- knn (train = train.trans[1:9],
		    cl    = train.trans$clase,
		    test  = test.trans[1:9],
		    k     = 1
	)
	mean (prd == test.trans$clase)
},
replications = 1000,
columns = c ("test", "replications", "elapsed",
            "relative", "user.self", "sys.self")
)

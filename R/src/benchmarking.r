# Started Thu  2 Jan 21:39:09 2020 by nahnero. #

suppressPackageStartupMessages (library (dplyr))
suppressPackageStartupMessages (library (tidyverse))
suppressPackageStartupMessages (library (caret))
suppressPackageStartupMessages (library (MASS))
suppressPackageStartupMessages (library (rbenchmark))
suppressPackageStartupMessages (library (class))

benchmark (
'1 load'= {
	datos <- read.table ('../../data.csv', sep = ',', header = T)
	datos <- na.omit (datos)
	datos <- datos %>% filter_all (all_vars (. <= quantile (., 0.99, na.rm = T)))
	p <- 0.7
},
'2 part'= {
	train.samples <- datos$clase %>% createDataPartition (p = p, list = F)
	train.data    <- datos[ train.samples,]
	test.data     <- datos[-train.samples,]
	preproc.param <- train.data %>% preProcess (method = c ("center", "scale"))
	train.trans   <- preproc.param %>% predict (train.data)
	test.trans    <- preproc.param %>% predict (test.data)
},
'3 lda' = {
	mdl <- lda (clase~., data = train.trans)
	prd <- mdl %>%  predict (test.trans)
	mean (prd$class == test.trans$clase)
},
'4 qda' = {
	mdl <- qda (clase~., data = train.trans)
	prd <- mdl %>%  predict (test.trans)
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

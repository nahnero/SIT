# Started Wed  1 Jan 19:27:33 2020 by nahnero. #
# load data
datos <- read.table ('../../data.csv', sep = ',', header = T)
datos <- na.omit (datos)

# remove outliers
suppressPackageStartupMessages (library (dplyr))
datos <- datos %>% filter_all (all_vars (. <= quantile (., 0.99, na.rm = T)))

suppressPackageStartupMessages (library (tidyverse))
suppressPackageStartupMessages (library (caret))
suppressPackageStartupMessages (library (MASS))

# Linear Discriminant Analysis
it <- 1000
ldascores <- rep (NA, times = it)
p <- 0.7 # partition
cat ('LDA\n')
pb <- txtProgressBar (min = 0, max = it, initial = 0, char = '|', style = 3)
for (i in 1:it){
train.samples <- datos$clase %>% createDataPartition (p = p, list = F)

train.data    <- datos[ train.samples,]
test.data     <- datos[-train.samples,]

preproc.param <- train.data %>% preProcess (method = c ("center", "scale"))

train.trans   <- preproc.param %>% predict (train.data)
test.trans    <- preproc.param %>% predict (test.data)

mdl <- lda (clase~., data = train.trans)

prd <- mdl %>%  predict (test.trans)

ldascores[i]  <- mean (prd$class == test.trans$clase)
setTxtProgressBar (pb, i)
}

# cat ('LDA', i, round (ldascores[i], 1), '\n')

# Quadratic Discriminant Analysis
qdascores <- rep (NA, times = it)
cat ('\nQDA\n')
pb <- txtProgressBar (min = 0, max = it, initial = 0, char = '|', style = 3)
for (i in 1:it){
train.samples <- datos$clase %>% createDataPartition (p = p, list = F)

train.data    <- datos[ train.samples,]
test.data     <- datos[-train.samples,]

preproc.param <- train.data %>% preProcess (method = c ("center", "scale"))

train.trans   <- preproc.param %>% predict (train.data)
test.trans    <- preproc.param %>% predict (test.data)

mdl <- qda (clase~., data = train.trans)

prd <- mdl %>%  predict (test.trans)

qdascores[i]  <- mean (prd$class == test.trans$clase)

setTxtProgressBar (pb, i)
}

# k Nearest Neighbours
knnscores <- rep (NA, times = it)
library (class)
cat ('\nKNN\n')
pb <- txtProgressBar (min = 0, max = it, initial = 0, char = '|', style = 3)
for (i in 1:it){
train.samples <- datos$clase %>% createDataPartition (p = p, list = F)

train.data    <- datos[ train.samples,]
test.data     <- datos[-train.samples,]

preproc.param <- train.data %>% preProcess (method = c ("center", "scale"))

train.trans   <- preproc.param %>% predict (train.data)
test.trans    <- preproc.param %>% predict (test.data)

prd <- knn (train = train.trans[1:9],
	    cl    = train.trans$clase,
	    test  = test.trans[1:9],
	    k     = 1)

knnscores[i]  <- mean (prd == test.trans$clase)

setTxtProgressBar (pb, i)
}
cat ('\n\n')

results <- data.frame (ldascores, qdascores, knnscores)
suppressPackageStartupMessages (library (psych))
print (describe (results))

# Results
suppressPackageStartupMessages (library (ggplot2))

results <- data.frame (xx = c (ldascores, qdascores, knnscores),
		       yy = rep (letters[1:3],each = 1000))

pdf ("../images/scores.pdf")
ggplot (results, aes (x = xx, fill = yy)) +
geom_density   (alpha = 0.7, adjust = 5) +
scale_fill_manual (values = c ('blue', 'red', 'green'),
		   labels = c ('LDA', 'QDA', 'KNN'),
		   name   = 'Method',
		   ) +
labs (x = 'score',  title = 'Densidad de Puntuación según método.') +
theme_bw () +
theme (panel.grid.major = element_blank(),
       panel.grid.minor = element_blank(),
       panel.background = element_rect(colour = "black", size = 1),
       )
dev.off ()

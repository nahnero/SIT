# Started Fri 17 Jan 12:13:18 2020 by nahnero. #
# Started Wed  1 Jan 19:27:33 2020 by nahnero. #
# load data
datos <- read.table ('../../data.csv', sep = ',', header = T)
datos <- na.omit (datos)

# remove outliers
suppressPackageStartupMessages (library (dplyr))
datos <- filter_all (datos, all_vars (. <= quantile (., 0.99, na.rm = T)))

suppressPackageStartupMessages (library (tidyverse))
suppressPackageStartupMessages (library (caret))
suppressPackageStartupMessages (library (MASS))

p <- 0.7 # partition
cat ('LDA\n')
train.samples <- createDataPartition (datos$clase, p = p, list = F)

train.data    <- datos[ train.samples,]
test.data     <- datos[-train.samples,]

preproc.param <- preProcess (train.data, method = c ("center", "scale"))

# train.trans   <- predict (preproc.param, train.data)
# test.trans    <- predict (preproc.param, test.data)

train.trans   <- train.data
test.trans    <- test.data

mdl <- lda (clase~., data = train.trans)

prd <- predict (mdl, test.trans)

score <- mean (prd$class == test.trans$clase)


suppressPackageStartupMessages (library (ROCR))
pred <- prediction (as.numeric (prd$class), as.numeric (test.trans$clase))
rocs <- performance (pred, "tpr", "fpr")

pdf ("../images/roc.pdf")
plot(rocs)
title ('Curva ROC R')
dev.off ()

auc_ROCR <- performance(pred, measure = "auc")
auc_ROCR@y.values[[1]]
suppressPackageStartupMessages (library (SDMTools))
mat <- confusion.matrix(as.numeric (prd$class) - 1 , as.numeric (test.trans$clase) - 1,threshold=0.5)
mat

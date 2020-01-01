# Started Mon 30 Dec 16:28:26 2019 by nahnero. #

# load data
datos <- read.table ('../../data.csv', sep = ',', header = T)
datos <- na.omit (datos)
suppressPackageStartupMessages (library (dplyr))
datos <- datos %>% filter_all (all_vars (. <= quantile (., 0.99, na.rm = T)))

library (car)
pdf ("../images/corrplot.pdf")
scatterplotMatrix (datos, regLine=list (col='red'), pch=20, cex=0.5, col='blue4')
dev.off ()

library (corrplot)
pdf ("../images/corrplot1.pdf")
M <- cor (na.omit (datos))
corrplot (M, method = 'number')
dev.off ()

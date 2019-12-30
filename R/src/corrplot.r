# Started Mon 30 Dec 16:28:26 2019 by nahnero. #

# load data
datos <- read.table ('../../data.csv', sep = ',', header = T)

pdf ("../images/corrplot.pdf")
plot (datos)
dev.off ()

library (corrplot)
pdf ("../images/corrplot1.pdf")
M <- cor (na.omit (datos))
corrplot (M, method = 'number')
dev.off ()

# Started Mon 30 Dec 16:28:26 2019 by nahnero. #

# load data
datos <- read.table ('../../data.csv', sep = ',', header = T)
library (ggplot2)

# boxplots
for (i in 1:10){
pdf (file = paste ('../images/hist', i, '.pdf', sep = ''), width = 6, height = 3)
print (ggplot (datos, aes (x = datos[,i], fill = as.factor (clase))) +
	       labs (x = NULL, y = NULL, title = names (datos)[i], fill = 'Clase') +
	       geom_histogram  (bins = 20, alpha = 0.6) +
	       theme_classic   (base_size = 20) +
	       scale_fill_manual(values = c ('green', 'blue')) +
	       theme   (legend.position = c (0.8, 1)))
dev.off ()
}

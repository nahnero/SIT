# Started Mon 30 Dec 16:28:26 2019 by nahnero. #

# load data
datos <- read.table ('../../data.csv', sep = ',', header = T)
library (ggplot2)

# boxplots
for (i in 1:10){
pdf (file = paste ('../images/qq', i, '.pdf', sep = ''), width = 6, height = 3)
print (ggplot (datos, aes (sample = datos[,i], colour = as.factor (clase))) +
	       labs (x = NULL, y = NULL,
		     title = names (datos)[i], colour = 'Clase') +
	       geom_qq () + geom_qq_line () + theme_classic (base_size = 20) +
	       scale_colour_manual (values = c ('green', 'blue')) +
	       theme   (legend.position = c (0.2, 0.85)))
dev.off ()
}

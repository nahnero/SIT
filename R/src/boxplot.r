# Started Mon 30 Dec 16:28:26 2019 by nahnero. #

# load data
datos <- read.table ('../../data.csv', sep = ',', header = T)
library (ggplot2)

# boxplots
for (i in 1:10){
pdf (file = paste ('../images/box', i, '.pdf', sep = ''), width = 6, height = 3)
print (ggplot (datos, aes (x = clase,
			   y = datos[,i],
			   group = clase)) +
	       labs (x = NULL, y = NULL, title = names (datos)[i]) +
	       geom_boxplot  () +
	       theme_classic (base_size = 20))
dev.off ()
}

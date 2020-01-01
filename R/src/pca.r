# Started Mon 30 Dec 16:28:26 2019 by nahnero. #
# load data
datos <- read.table ('../../data.csv', sep = ',', header = T)
datos <- na.omit (datos)

# PCA
pca <- prcomp (datos[,1:9], center = T, scale. = T, rank. = 9)
summary (pca)


# Pareto
pdf ("../images/pareto.pdf", width = 7, height = 5.5)
x  <- pca[['sdev']]^2
cx <- cumsum (x)
par (mar = c(3,3,4,3))
pc <- barplot (x, names.arg = dimnames (pca[['rotation']])[[2]],
	       border = NA, axes = F, main = 'Pareto R',
	       ylim = c(0, 1.05*max(cx, na.rm = T)), col = 'blue4'
)
lines (pc, cx, type = 'b', pch = 19, col="red")
box  (col    = 'black')
axis (side   = 2,
      at     = c (0, round (x[c (1,2,4,6,8,9)], 1)),
      las    = 2, cex.axis = 0.8,
)
axis (side   = 4,
      at     = c(0, cx[1:8]),
      labels = paste (c (0, round (cx[1:8]/max (cx) * 100)) ,"%",sep=""),
      las    = 2, cex.axis = 0.8
)
dev.off ()

# Biplot
library (ggfortify)
pdf ("../images/biplot.pdf", width = 6, height = 5)
autoplot (pca, data = datos, colour = 'clase',
	  loadings  = T,
	  main      = 'Biplot R',
	  loadings.label        = T,
	  loadings.label.repel  = T,
	  loadings.label.colour = 'green4',
) +
theme_bw () +
theme (panel.grid.major = element_blank(),
       panel.grid.minor = element_blank(),
       panel.background = element_rect(colour = "black", size = 1),
       legend.position  = 'none'
)
dev.off ()

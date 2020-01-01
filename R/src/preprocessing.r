# Started Wed  1 Jan 21:40:44 2020 by nahnero. #
# load data
datos <- read.table ('../../data.csv', sep = ',', header = T)
datos <- na.omit (datos)

# ignore rows w/ components above the $\color[HTML]{228B22}99^{th}$ percentile
suppressPackageStartupMessages (library (dplyr))
datos <- datos %>% filter_all (all_vars (. <= quantile (., 0.99, na.rm = T)))

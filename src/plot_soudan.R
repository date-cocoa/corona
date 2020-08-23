library(tidyverse)

df <- read_csv('../data/data_sodan.csv')

my_theme <-
  theme_bw(base_family = "HiraKakuProN-W3") + 
  theme(axis.text = element_text(size = 10),
        axis.title = element_text(size = 10), 
        axis.ticks.length=unit(0.2, "cm"))
theme_set(my_theme) 

title = paste0('発熱等相談件数_', Sys.Date())

g <- 
  df %>% 
  ggplot() + 
  geom_line(aes(x = date, y = number, color = week)) +
  ggtitle(title) +
  xlab('month')

ggsave('../img/soudan.png', width = 9, height = 5)

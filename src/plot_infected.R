library(tidyverse)

url <- 'https://stopcovid19.metro.tokyo.lg.jp/data/130001_tokyo_covid19_patients.csv'
data <- read_csv(url)

my_theme <-
  theme_bw(base_family = "HiraKakuProN-W3") + 
  theme(axis.text = element_text(size = 10),
        axis.title = element_text(size = 10), axis.ticks.length=unit(0.5, "cm"))
theme_set(my_theme) # set theme

title <- paste0('報告感染者数_', Sys.Date())

g <- 
  data %>% 
  select(公表_年月日, 曜日) %>% 
  group_by(公表_年月日, 曜日) %>% 
  count() %>% 
  ggplot() + 
  geom_line(aes(x = 公表_年月日,  y = n, color = 曜日)) + 
  scale_color_discrete(breaks=c('月', '火', '水', '木', '金', '土', '日')) +
  ggtitle(title)

ggsave('./img/infected.png', width = 9, height = 5)

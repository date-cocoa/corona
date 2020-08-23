# corona
コロナウイウルスに関するスクリプト。./src/配下で実行すること。\

## 実行順
### 発熱等相談件数の場合
```zsh
python get_data_soudan.py
Rscript plot_soudan.R
open ../img/soudan.png
```

### 報告感染者数の場合
```zsh
Rscript plot_infected.R
open ../img/infected.png
```

[![PyPI version](https://badge.fury.io/py/hydrohyeto-matplotlib.svg)](https://badge.fury.io/py/hydrohyeto-matplotlib.svg)
# hydrohyeto_matplotlib
ハイドロ、ハイエトグラフをmatplotlibで表示します。

![demo](https://github.com/yakitoritabetai/hydrohyeto-matplotlib/blob/master/demo.png?raw=true "demo")

## 利用方法
- hydrohyeto_matplotlibをimportした後、hydrohyetoを実行します。
- グラフのラベルや凡例等のパラメータはコードの「default_kwargs」を参照してください。

```python
import hydrohyeto_matplotlib
import pandas as pd

df_o = pd.read_csv(f'demo.csv', parse_dates=['date'], index_col=0)

zz = {
    'label_real': '実測値',
    'title': 'デモ用',
}
fig = hydrohyeto_matplotlib.hydrohyeto(
    df_o,
    **zz
)
fig.savefig('demo.png')
```




## インストール
```sh
# pip
pip install hydrohyeto-matplotlib
```

## 利用フォント
IPAフォントのIPAexゴシック(Ver.003.01)を利用しています。
利用にあたっては[IPAフォントライセンスv1.0](https://github.com/uehara1414/japanize-matplotlib/blob/master/japanize_matplotlib/fonts/IPA_Font_License_Agreement_v1.0.txt)に同意してください。

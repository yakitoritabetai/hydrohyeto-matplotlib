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
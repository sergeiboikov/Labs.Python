import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.ticker import FormatStrFormatter, LinearLocator, FuncFormatter


df = pd.read_csv("F:\GIT\Labs.Python\Weather Analysis\source.csv", sep=',', encoding='utf-8')
cityname = 'Saratov'
df = df[(df['Year'] >= 2006)]

plt.rcParams["figure.figsize"] = (8, 5)
fig, ax = plt.subplots()

def neg_tick(x, pos):
    return '%.1f' % (-x if x else 0)

plt.bar(df['Year'].values, -df['Jan'].values, label=f'{cityname} - January Temperature, C')
plt.plot(df['Year'].values, -df['Jan'].rolling(window=20, min_periods=1).mean(), 'r-')
ax.yaxis.set_major_formatter(FuncFormatter(neg_tick))

plt.legend(loc='best')
plt.tight_layout()
plt.show()
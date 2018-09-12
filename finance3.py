import datetime as dt 
import matplotlib.pyplot as plt 
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web


style.use('ggplot')

df = pd.read_csv('AMD.csv', parse_dates= True, index_col=1) #changed to 1 due to col 0 being symbol

df['100 MA'] = df['close_price'].rolling(window=100, min_periods=0).mean()

print(df.head())

ax1 = plt.subplot2grid((6,1), (0,0), rowspan=5, colspan=1)
ax2 = plt.subplot2grid((6,1), (5,0), rowspan=1, colspan=1, sharex=ax1)

ax1.plot(df.index, df['close_price'])
ax1.plot(df.index, df['100 MA'])
ax2.bar(df.index, df['volume'])

plt.show()
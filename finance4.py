import datetime as dt 
import matplotlib.pyplot as plt 
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web
from matplotlib.finance import candlestick_ohlc
import matplotlib.dates as mdates

style.use('ggplot')

df = pd.read_csv('AMD.csv', parse_dates= True, index_col=1)

df['100 MA'] = df['close_price'].rolling(window=100, min_periods=0).mean()

df_ohlc = df['close_price'].resample('10 D').ohlc()
df_volume = df['volume'].resample('10 D').sum()

df_ohlc.reset_index(inplace=True)
df_ohlc['begins_at'] = df_ohlc['begins_at'].map(mdates.date2num)


ax1 = plt.subplot2grid((6,1), (0,0), rowspan=5, colspan=1)
ax2 = plt.subplot2grid((6,1), (5,0), rowspan=1, colspan=2, sharex=ax1)
ax1.xaxis_date()

candlestick_ohlc(ax1, df_ohlc.values,width=2,colorup='g')
ax2.fill_between(df_volume.index.map(mdates.date2num), df_volume.values,0)

plt.show()
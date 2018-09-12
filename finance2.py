import datetime as dt 
import matplotlib.pyplot as plt 
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web


style.use('ggplot')

start = dt.datetime(2018,9,1)
end =dt.datetime.now()

df = pd.read_csv('AMD.csv', parse_dates= True, index_col=0)


df['Close'].plot()
plt.show()
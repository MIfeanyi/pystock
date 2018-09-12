import datetime as dt 
import matplotlib.pyplot as plt 
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web


style.use('ggplot')

start = dt.datetime(2018,1,1)
end =dt.datetime.now()

df = web.DataReader('AMD','robinhood',start,end)
print(df.tail(6))
df.to_csv('AMD.csv')
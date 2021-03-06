import bs4 as bs
import datetime as dt
import os
import pandas as pd
import pandas_datareader.data as web
import pickle
import requests

def save_sp500_tickers():
    resp = requests.get('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
    soup = bs.BeautifulSoup(resp.text, 'lxml')
    table = soup.find('table',{'class':'wikitable sortable'})
    tickers = []
    for row in table.findAll('tr')[1:]:
        ticker = row.findAll('td')[0].text
        tickers.append(ticker)
    
    with open('sp500tickers.pickle','wb') as f:
        pickle.dump(tickers,f)
    print(tickers)
    return tickers


#save_sp500_tickers()

def get_data_from_ms(reload_sp500=False,reload_all=False):
    if reload_sp500:
        tickers = save_sp500_tickers()
    else:
        with open('sp500tickers.pickle','rb') as f:
            tickers = pickle.load(f)
    if not os.path.exists('stock_dfs'):
        os.makedirs('stock_dfs')
    start = dt.datetime(2000,1,1)
    end =dt.datetime.now()

    for ticker in tickers:
        if not os.path.exists('stock_dfs/{}.csv'.format(ticker)):
            print('added {}'.format(ticker))
            try:
                df = web.DataReader(ticker.encode('utf8'),'robinhood',start,end,retry_count=0)
                print(df.tail(5))
                df.to_csv('stock_dfs/{}.csv'.format(ticker))
            except ValueError:
                print('${} unavailable'.format(ticker))
        else:
            print('Already exists {}'.format(ticker))

get_data_from_ms()
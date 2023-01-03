from polygon import RESTClient
import config
import pandas as pd


client = RESTClient(config.API_KEY)


api = config.API_KEY
ticker = None
limit = 1000
market = 'stocks'
type = 'CS'
exchange = 'XNAS'

tickers = []
for ticker in client.list_tickers(type='CS',market='stocks',limit=1000,exchange='XNAS'):
    tickers.append(ticker)
    
df = pd.DataFrame(tickers)
listOfTickers = df['ticker']
dflistOfTickers = pd.DataFrame(listOfTickers)

marketCaps = []
i=0
for ticker in listOfTickers:
     marketCaps.append(client.get_ticker_details(ticker=ticker).market_cap)
     i += 1
     print('running',i)

dflistOfTickers['marketCap'] = marketCaps
dflistOfTickers.to_csv('tickersAndMarketcaps.csv',index=False)

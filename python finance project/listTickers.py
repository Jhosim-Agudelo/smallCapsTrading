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


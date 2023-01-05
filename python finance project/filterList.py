from polygon import RESTClient
import config
import pandas as pd


client = RESTClient(config.API_KEY)

dflistOfTickers = pd.read_csv('tickersLt250M_copy.csv')

dflistOfTickersLt250M = dflistOfTickers[dflistOfTickers['marketCap']<250000000]


listTickersLt250M =[]
for ticker in dflistOfTickersLt250M['ticker']:
    listTickersLt250M.append(ticker)


print(listTickersLt250M)
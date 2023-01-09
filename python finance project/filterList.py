from polygon import RESTClient
import config
import pandas as pd


client = RESTClient(config.API_KEY)
dflistOfTickers = pd.read_csv('tickersAndMarketCaps.csv')


def makeList(dflistOfTickers,lower_bound_MktCap,upper_bound_MktCap):
    df =dflistOfTickers[dflistOfTickers['marketCap']<upper_bound_MktCap]
    df = dflistOfTickers[dflistOfTickers['marketCap']>lower_bound_MktCap]
    list=[]
    for ticker in df['ticker']:
        list.append(ticker)
    return list

listTickersLt250M = makeList(dflistOfTickers,0,250000000)


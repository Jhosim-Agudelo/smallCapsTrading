from polygon import RESTClient
import config
import pandas as pd
from listTickers import listOfTickers


client = RESTClient(config.API_KEY)
test= ['AAL','ZYNE','TSLA']
list = []
for ticker in listOfTickers:
    list.append(client.get_daily_open_close_agg(ticker=ticker,date='2022-12-28'))
print(list)
'''
previousClose = client.get_previous_close_agg(ticker='TSLA')
df = pd.DataFrame(previousClose)
df['date']= df['timestamp'].apply(lambda x: pd.to_datetime((x-3600000*5)*1000000))
df = df.set_index('date')
'''


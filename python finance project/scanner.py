from polygon import RESTClient
import config
import pandas as pd
import datetime
from filterList import listTickersLt250M
from concurrent.futures import ThreadPoolExecutor

client = RESTClient(config.API_KEY)

test = ['TSLA','AAPL','ZYNE','ZTEK']
list = []
# choose the range date that you want to use
start_date = '2022-11-01'
end_date = '2022-11-30'

start_date = datetime.datetime.strptime(start_date, '%Y-%m-%d')
end_date = datetime.datetime.strptime(end_date, '%Y-%m-%d')
#print((end_date - start_date).days)
c = 0


def get_data(stock,date):
        try:
            return list.append(client.get_daily_open_close_agg(stock,date))
        except: 
            print(stock,'No data on this day')
            return None

def set_date_range(start_date,end_date):
    for day in range((end_date - start_date).days + 1):
        current_day = start_date + datetime.timedelta(days=day)
        current_day_str = current_day.strftime('%Y-%m-%d')
        return current_day_str



with ThreadPoolExecutor() as executor:
    for stock in test:  
        for day in range((end_date - start_date).days + 1):
            c +=1
            print('get request number: ',c, ' ticker: ',stock)
            current_day = start_date + datetime.timedelta(days=day)
            current_day_str = current_day.strftime('%Y-%m-%d')
            executor.submit(get_data, stock, current_day_str)


df = pd.DataFrame(list)
df = df.set_index('symbol')
df = df.loc[:,["from_","open","close","high","low","pre_market","after_hours","volume","status","otc"]]
df.to_csv(current_day_str+'.csv')
print(df)
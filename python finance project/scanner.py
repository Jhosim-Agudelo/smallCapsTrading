from polygon import RESTClient
import config
import pandas as pd
import datetime
from filterList import listTickersLt250M


client = RESTClient(config.API_KEY)


test2 = ['ZTEK']


list = []
# choose the range date that you want to use
start_date = '2022-10-01'
end_date = '2022-10-31'

start_date = datetime.datetime.strptime(start_date, '%Y-%m-%d')
end_date = datetime.datetime.strptime(end_date, '%Y-%m-%d')
#print((end_date - start_date).days)
c = 0
for stock in listTickersLt250M:  
    for day in range((end_date - start_date).days + 1):
        c +=1
        print('get request number: ',c, ' ticker: ',stock)
        current_day = start_date + datetime.timedelta(days=day)
        current_day_str = current_day.strftime('%Y-%m-%d')
        try:
            list.append(client.get_daily_open_close_agg(stock,date=current_day_str))
        except: print(stock,'No data on this day')

df = pd.DataFrame(list)
df = df.set_index('symbol')
df.to_csv(current_day_str+'.csv')
print(df)
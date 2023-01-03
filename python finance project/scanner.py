from polygon import RESTClient
import config
import pandas as pd
from listTickers import listOfTickers
import datetime


client = RESTClient(config.API_KEY)
test= ['AAL']
list = []


start_date = '2022-12-05'
end_date = '2022-12-09'

start_date = datetime.datetime.strptime(start_date, '%Y-%m-%d')
end_date = datetime.datetime.strptime(end_date, '%Y-%m-%d')
print((end_date - start_date).days)

for day in range((end_date - start_date).days + 1):
    current_day = start_date + datetime.timedelta(days=day)
    current_day_str = current_day.strftime('%Y-%m-%d')
    print(current_day_str)
    for ticker in test:
        list.append(client.get_daily_open_close_agg(ticker=ticker,date=current_day_str))


list = pd.DataFrame(list)
list = list.set_index('symbol')

print(list)
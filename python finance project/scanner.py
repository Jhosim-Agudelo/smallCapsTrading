from polygon import RESTClient
import config
import pandas as pd
import datetime


client = RESTClient(config.API_KEY)

tickers= pd.read_csv('tickersLt250M_copy.csv')
listofTickers = tickers['ticker'].to_list()
list = []
# choose the range date that you want to use
start_date = '2022-01-03'
end_date = '2022-01-07'

start_date = datetime.datetime.strptime(start_date, '%Y-%m-%d')
end_date = datetime.datetime.strptime(end_date, '%Y-%m-%d')
#print((end_date - start_date).days)


for ticker in listofTickers:
    print('ticker: '+ ticker )
    for day in range((end_date - start_date).days + 1):
        current_day = start_date + datetime.timedelta(days=day)
        current_day_str = current_day.strftime('%Y-%m-%d')

        list.append(client.get_daily_open_close_agg(ticker=ticker,date=current_day_str))



list = pd.DataFrame(list)
list = list.set_index('symbol')
list.to_csv('openClose.csv"',index= True)

print(list)
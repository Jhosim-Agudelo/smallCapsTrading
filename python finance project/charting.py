from polygon import RESTClient
import config
from plotly import graph_objects as go
import pandas as pd
import pandas_ta as ta
from plotly.subplots import make_subplots

client = RESTClient(config.API_KEY)

def createFig():
    fig = make_subplots(rows=2, cols=1, 
                        shared_xaxes=True,vertical_spacing=0.01, 
                        row_heights=[0.5,0.1])
    return fig


def plot(df,ticker,fig):
    fig.add_trace(go.Candlestick(
                x = df.index,
                open = df['open'],high = df['high'],
                low = df['low'],close = df['close']),
                row=1,col=1)
    df['200EMA']=ta.ema(df['close'],length=200)
    fig.add_trace(go.Scatter(x = df.index, y = df['200EMA'], opacity = 0.7, line = dict(color = 'white', width = 2)),row = 1, col = 1)
    
    fig.add_trace(go.Bar(x=df.index,y=df['volume'],marker_color='red'),row = 2, col = 1)
    fig.update_xaxes(rangebreaks=[dict(bounds=["sat", "mon"])])
    fig.update_layout(xaxis_rangeslider_visible=False, template = 'plotly_dark')
    fig.update_layout(title= str(ticker))
    fig.show()
    #fig.write_image(ticker+'.png')
    


def jLinesFiveMin(df,fig):
    df['14EMA']=ta.ema(df['close'],length=14)
    df['17EMA']=ta.ema(df['close'],length=17)
    df['41EMA']=ta.ema(df['close'],length=41)
    df['51EMA']=ta.ema(df['close'],length=51)
    df['72EMA']=ta.ema(df['close'],length=72)
    df['89EMA']=ta.ema(df['close'],length=89)

    fig.add_trace(go.Scatter(x = df.index, y = df['14EMA'], opacity = 0.7, line = dict(color = 'purple', width = 2)),row = 1, col = 1)
    fig.add_trace(go.Scatter(x = df.index, y = df['17EMA'], opacity = 0.7, line = dict(color = 'purple', width = 2)),row = 1, col = 1)
    fig.add_trace(go.Scatter(x = df.index, y = df['41EMA'], opacity = 0.7, line = dict(color = 'green', width = 2)),row = 1, col = 1)
    fig.add_trace(go.Scatter(x = df.index, y = df['51EMA'], opacity = 0.7, line = dict(color = 'green', width = 2)),row = 1, col = 1)
    fig.add_trace(go.Scatter(x = df.index, y = df['72EMA'], opacity = 0.7, line = dict(color = 'orange', width = 2)),row = 1, col = 1)
    fig.add_trace(go.Scatter(x = df.index, y = df['89EMA'], opacity = 0.7, line = dict(color = 'orange', width = 2)),row = 1, col = 1)


def jLinesOneMin(df,fig):
    df['72EMA']=ta.ema(df['close'],length=72)
    df['89EMA']=ta.ema(df['close'],length=89)
    df['216EMA']=ta.ema(df['close'],length=216)
    df['267EMA']=ta.ema(df['close'],length=267)
    df['360EMA']=ta.ema(df['close'],length=360)
    df['445EMA']=ta.ema(df['close'],length=445)

    fig.add_trace(go.Scatter(x = df.index, y = df['72EMA'], opacity = 0.7, line = dict(color = 'purple', width = 2)),row = 1, col = 1)
    fig.add_trace(go.Scatter(x = df.index, y = df['89EMA'], opacity = 0.7, line = dict(color = 'purple', width = 2)),row = 1, col = 1)
    fig.add_trace(go.Scatter(x = df.index, y = df['216EMA'], opacity = 0.7, line = dict(color = 'green', width = 2)),row = 1, col = 1)
    fig.add_trace(go.Scatter(x = df.index, y = df['267EMA'], opacity = 0.7, line = dict(color = 'green', width = 2)),row = 1, col = 1)
    fig.add_trace(go.Scatter(x = df.index, y = df['360EMA'], opacity = 0.7, line = dict(color = 'orange', width = 2)),row = 1, col = 1)
    fig.add_trace(go.Scatter(x = df.index, y = df['445EMA'], opacity = 0.7, line = dict(color = 'orange', width = 2)),row = 1, col = 1)





def plotChart(ticker,multiplier,timespan,from__,to_,):

    resp = client.get_aggs(ticker,multiplier,timespan, from_=from__,to=to_)

    df = pd.DataFrame(resp)
    df['date']= df['timestamp'].apply(lambda x: pd.to_datetime((x-3600000*5)*1000000))
    df = df.set_index('date')
    fig = createFig()
    
    if multiplier == 5 and timespan == 'minute':
        jLinesFiveMin(df,fig)
        return plot(df,ticker,fig)
    elif multiplier ==1 and timespan == 'minute':
        jLinesOneMin(df,fig)
        return plot(df,ticker,fig)
    else: return plot(df,ticker,fig)



plotChart('KALA',1,'minute', '2022-12-28','2022-12-30')

import time
import requests
import pandas as pd
import random
from io import StringIO


stocks=['INFY','TCS','ABB','ABAN','TITAN','HCC','NCC']


done=[]


def alpha_puller(s):
    #time.sleep(1.65)
    a = requests.get('https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol='+s+'.NS&interval=1min&apikey='+random.choice(api_keys)+'&datatype=csv&outputsize=full').text
    d = pd.read_csv(StringIO(a),skiprows=range(1),names =['tdate','Open','High','Low','Close','Volume'])
    d.tdate = pd.to_datetime(d.tdate)
    d.tdate = d.tdate+pd.Timedelta(minutes=30)+pd.Timedelta(hours=9)
    d['Date'] = d.tdate.dt.strftime('%Y%m%d')
    d['Time'] = d.tdate.dt.strftime('%H%M%S')
    d = d.iloc[::-1]
    d = d[['Date','Time','Open','High','Low','Close','Volume']]
    d.to_csv('/path/to/save'.csv' ,index=False)
    print(s)

    
stocks.sort()
while not stocks==done:
    for i in stocks:
        if i not in done:
            try:
                alpha_puller(i)
                done.append(i)
            except (ValueError, ConnectionError) as e:
                time.sleep(4)
                try:
                    alpha_puller(i)
                    done.append(i)
                except (ValueError, ConnectionError) as e:
                    #print(i+' missed')
                   time.sleep(5)
                   try:
                       alpha_puller(i)
                       done.append(i)
                   except:
                       print(i+' missed')
    done.sort()

# adjust for day-light savings in data from 2018-11-05

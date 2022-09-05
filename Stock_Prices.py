import requests
from bs4 import BeautifulSoup
import pandas as pd
import datetime


class stock_download:
    name = "Stocks_Downloader"
    
    def __init__(self,update,price,change,change_percent,record_time):
        self.update = update
        self.price = price
        self.change = change
        self.change_percent = change_percent
        self.record_time = record_time



    def get_data(symbol):
        # Set the site to crape the data from
        url = 'https://www.marketwatch.com/investing/stock/' + symbol
        r = requests.get(url)
        soup = BeautifulSoup(r.text,'html.parser')
        #Read The data
        
        try:
            update = [soup.find('div',{'class':'intraday__timestamp'}).find_all('bg-quote')[0].text]
            price = soup.find('div', {'class':'intraday__data'}).find_all('span')[0].text
            change_ = soup.find('div', {'class':'intraday__data'}).find_all('span')[1].text
            change_percent_ = soup.find('div', {'class':'intraday__data'}).find_all('span')[2].text
            date_get = [datetime.datetime.now()]
        except:
            update = [soup.find('div',{'class':'intraday__timestamp'}).find_all('bg-quote')[0].text]
            price = soup.find('div', {'class':'intraday__data'}).find_all('bg-quote')[0].text
            change_ = soup.find('div', {'class':'intraday__data'}).find_all('span')[0].text
            change_percent_ = soup.find('div', {'class':'intraday__data'}).find_all('span')[1].text
            date_get = [datetime.datetime.now()]
        
        
        if "," in price:
            price = [float(price.replace(",",""))]
        else:
            price = [float(price)]
        
        change_ = [float(change_)]
        change_percent_ =[float(change_percent_.replace('%',""))]
        
        
        
        frame = pd.DataFrame(
            {
                'date_get':date_get,
                'update': pd.to_datetime(update),
                'symbol': [symbol],
                'price':price,
                'change': change_,
                'change_percent_':change_percent_
            })

        return frame








    





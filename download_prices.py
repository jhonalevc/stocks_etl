import pandas as pd
import numpy as np
import Stock_Prices as sp
import datetime
from sqlalchemy import create_engine

# Define variables for sql connection.
user= 'postgres'
password = 'Alejandro123!'
ip = '34.71.5.205'

#Connect to the DB.
engine = create_engine(
    'postgresql+psycopg2://' + user + ':'+ password +'@'+ ip +'/postgres')

#Download portfolio. 
portfolio = pd.read_sql("""SELECT * FROM public.portfolio""",  con = engine)

#Extract Data from the Web 
def download_data(dataframe):
    """ Get the current information """
    global date_time
    date_time = datetime.datetime.now()
    frames = []
    Errors = []
    list_of_symbols = dataframe['Symbol']
    for symbol in list_of_symbols:
        try:
            frames.append(sp.stock_download.get_data(symbol))
        except:
            try:
                Errors.append(
                    pd.DataFrame({
                        'datetime' : [date_time],
                        'symbol' :[symbol]
                    })
                )
            except:
                Errors.append(
                    pd.DataFrame({'datetime':[date_time], 'symbol':[np.nan]})
                )
    exchange = pd.concat(frames)
    exchange['run'] = date_time
    try:
        errors = pd.concat(Errors)
    except:
        errors = pd.DataFrame({'datetime':[date_time], 'symbol':[np.nan]})
    end_datetime = datetime.datetime.now()    
    elapsed_time = end_datetime - date_time
    try:
        hours = elapsed_time.hours
    except:
        hours = 0
    try:
        minutes = elapsed_time.minutes
    except:
        minutes = 0
    try:
        seconds = elapsed_time.seconds
    except:
        seconds = 0
    elapsed_time = 'Took ' + str(hours) + ' hours, ' + str(minutes) + ' minutes, ' + str(seconds) + ' seconds'
    return   exchange, errors, elapsed_time



#load_the_data
def load_data(data):
    ''' Upload the data to the DB'''
    print("Scrape the data from the Web")
    exchange, errors, elapsed_time = download_data(data)
    exchange.to_sql(
        index = False,
        con = engine,
        schema = 'public',
        name = 'exchange',
        if_exists='append')

    errors.to_sql(
        index = False,
        con = engine,
        schema = 'public',
        name = 'errors',
        if_exists='append')

    pd.DataFrame({'datetime':[date_time],'Duration':[elapsed_time]}).to_sql(
        index = False,
        con = engine,
        schema = 'public',
        name = 'time',
        if_exists='append'
    )




if __name__ == "__main__":

    load_data(portfolio.sample(10))
    print('Done!')
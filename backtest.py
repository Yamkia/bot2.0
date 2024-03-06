import MetaTrader5 as mt5
import pandas as pd
from datetime import datetime
import send_orders



def fetch_data(symbol, timeframe, start_date, end_date):
    
    mt5.symbol_select(symbol)
    mt5.copy_rates_range(symbol, timeframe, start_date, end_date)
    rates = mt5.copy_rates_from_pos(symbol, timeframe, 0, 1000)
    data = pd.DataFrame(rates)
    data['time'] = pd.to_datetime(data['time'], unit='s')
    data.set_index('time', inplace=True)

    return data




  
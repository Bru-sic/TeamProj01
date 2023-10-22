import pandas as pd
from alpha_vantage.timeseries import TimeSeries


def get_stock_data(tickers, start_date, end_date, api_key):
    ts = TimeSeries(key=api_key, output_format='pandas')

    # Initialize an empty dictionary to store data for each ticker
    ticker_data = {}

    # Retrieve data for each ticker and store it in the dictionary
    for tick in tickers:
        data, meta_data = ts.get_daily(symbol=tick, outputsize='full')
        data = data[(data.index >= start_date) & (data.index <= end_date)]
        ticker_data[tick] = data

    # Rename columns using the 'column_names' dictionary
    column_names = {
        '1. open': 'open',
        '2. high': 'high',
        '3. low': 'low',
        '4. close': 'close',
        '5. volume': 'volume'
    }

    for ticker in tickers:
        ticker_data[ticker].rename(columns=column_names, inplace=True)

    # Combine the data and assign column names
    combined_data = pd.concat(ticker_data, axis=1, keys=tickers)

    # Set the column name levels
    combined_data.columns.names = ['Ticker', 'Stock Info']

    return combined_data


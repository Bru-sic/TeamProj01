# Import libraries and dependencies
import alpaca_trade_api as tradeapi
from alpha_vantage.timeseries import TimeSeries

def create_alpaca_api(api_key, api_secret, base_url):
    """
    Create an Alpaca API object using the provided API key and secret.
    
    Args:
        api_key (str): Your Alpaca API key.
        api_secret (str): Your Alpaca API secret key.
        
    Returns:
        tradeapi.REST: Alpaca API object.
    """
    alpaca = tradeapi.REST(
        api_key,
        api_secret,
        base_url,
        api_version="v2"
    )
    return alpaca

def get_historical_data(api, tickers, timeframe, start_date, end_date):
    """
    Get historical data for a list of tickers within the specified date range.
    
    Args:
        api (tradeapi.REST): Alpaca API object.
        tickers (list): List of ticker symbols.
        timeframe (str): Timeframe (e.g., "1Min", "1Hour", "1Day").
        start_date (str): Start date in ISO format.
        end_date (str): End date in ISO format.
        
    Returns:
        pd.DataFrame: Historical data for the specified tickers.
    """
    df = api.get_bars(
        tickers,
        timeframe,
        start=start_date,
        end=end_date
    ).df
    return df











import pandas as pd
from NewForecastTools import MCSimulation
from datetime import datetime

def create_monte_carlo_simulation(df_ticker):
    # Prompt the user for input
    year = int(input("Enter number of year (e.g., 1): "))
    num_simulations = int(input("Enter number of simulations (e.g., 500): "))
    num_assets = int(input("Enter the number of assets: "))
    weights = []

    for i in range(num_assets):
        weight = float(input(f"Enter the weight for asset {i + 1} (e.g., 0.60): "))
        weights.append(weight)

    # Create the Monte Carlo Simulation
    num_simulations = num_simulations
    num_trading_days = 252 * year
    weights = weights

    MC_by_num_year = MCSimulation(
        portfolio_data=df_ticker,
        weights=weights,
        num_simulation=num_simulations,
        num_trading_days=num_trading_days
    )

    return MC_by_num_year

# Usage example
# Rename mc_simulation to suit number of year 
#mc_simulation = create_monte_carlo_simulation(your_portfolio_in_pd.dataFrame)

def get_user_dates():
    date_input = input("Enter a date (YYYY-MM-DD): ")
    
    try:
        timestamp = pd.Timestamp(date_input, tz="America/New_York")
        date_str = timestamp.strftime("%Y-%m-%d")
        return datetime.strptime(date_str, '%Y-%m-%d')
    except ValueError:
        return "Invalid date format. Please use YYYY-MM-DD format."

#Usage    
#start_date_string = get_user_dates() 
#end_date_string = get_user_dates()    

def get_user_input_tickers():
    tickers = []
    num_tickers = int(input("Enter the number of tickers: "))
    
    for i in range(num_tickers):
        ticker = input(f"Enter ticker {i + 1}: ")
        tickers.append(ticker)
    
    return tickers

# Example usage:
# user_tickers = get_user_input_tickers()

def year():
        # Prompt the user for input
        year = int(input("Enter number of year (e.g., 1): "))
        return year

def num_simulations():
    # Prompt the user for input
    num_simulations = float(input("Enter the number of simulations (e.g., 500): "))
    num_assets = int(input("Enter the number of assets: "))
    weights = []

    for i in range(num_assets):
        weight = float(input(f"Enter the weight for asset {i + 1} (e.g., 0.60): "))
        weights.append(weight)

    return num_simulations

def weights():
    # Prompt the user for input
    num_assets = int(input("Enter the number of assets: "))
    weights = []

    for i in range(num_assets):
        weight = float(input(f"Enter the weight for asset {i + 1} (e.g., 0.60): "))
        weights.append(weight)

    return weights


def get_user_input_one_ticker(stock_data):
    while True:
        try:
            ticker = input("Enter a stock ticker: ").strip().upper()
            
            if ticker in stock_data.columns.get_level_values(0):
                return ticker
            else:
                print("Invalid ticker. Please enter a valid ticker from the list.")
        except ValueError:
            print("Invalid input. Please enter a valid stock ticker.")
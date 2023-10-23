# Group Project 1

Authors: Bruno Ivasic, Kay Levin, Nazeer Wajahat   

Instructor: Nicholas J Creed

Date: 23 October 2023

# Contents


# Project Proposal
Our project is to perform a health check and expected returns of a portfolio consisting of securities. We will determine the overall portfolio’s performance to date as well as the performance of each individual security in the portfolio. Although aspects of this project are similar to the Module 05 assignment, our point of differentiation is how we intend to structure the data, to use more advanced charting, and problem solve certain aspects desirable to an amateur investor, including portfolio rebalancing recommendations. 

* Our project is to perform a portfolio analysis containing a list of stocks. 
* Our app fetches current and historical data to determine the past performance, current value and future forecasting of a portfolio of securities.
* Nice to have: Our app allows rebalancing of the portfolio based on a target portfolio weighting, suggesting which stocks to buy or sell, and sending the instructions to the trading platform.
* Nice to have: Our app presents a dashboard of comparative performance indicators on the portfolio
* Our app needs stock market data including:
  * Current and historical prices (open, high, low, close)
  * Trading volumes (volume, number of trades, volume-weighted average price (VWAP))
  * Nice to have: Other performance and valuation measure such as Price / Earnings ratios, Price / Book ratios, and Yield. Having Cum/Ex Dividend status and stock split dates will help adjust our analysis for any stock splits
* The kind of questions we will be asking of that data will include:
  * How the portfolio is fairing compared to a benchmark market index (eg S&P500)
  * How has the portfolio performed to date
  * What is the current value of the portfolio
  * What needs to happen to rebalance the portfolio to an ideal target weighting set by the investor 
  * Where could the portfolio be at a future date based on past performance and volatility 
* Possible sources for such data includes Alpaca Markets, NASDAQ, ASX, Binance 

# Dependencies
Starting the project:
```conda activate dev```

```pip install pandas==1.1.5 numpy==1.19.4 scipy==1.5.4```

```pip install python-dotenv```
```pip install PyPortfolioOpt==1.5.5```

```pip install datetime```
```pip install ipywidgets```
```pip install seaborn```
```pip install matplotlib```
```pip install alpha_vantage```

# Troubleshooting

* Error ```"ModuleNotFoundError: No module named 'alpaca_trade_api'``` encountered when running script.
From the gitbash terminal window run the following:   
`conda activate dev`   
`pip3 install alpaca-trade-api`

# Examples of the Application
[Main Code Module](./Code/main.ipynb)
[User Interface Minimum Viable Product](./Code/ui.ipynb)

## Application Conclusions
Wer have presented an application that has outperformed the average investor and the base market index using Efficient Frontier.

# Presentation
[PowerPoint Presentation](./Presentation/Project%20Presentation.pptx)

# Acknowledgements
## Source Code Attribution
* NewForecastTools module sourced from the experimental tools folder under "01-Lessons/05-APIs/3/New Tools (Experimental)"
* Alpaca Markets API documentation:  https://github.com/alpacahq/alpaca-trade-api-python/#alpaca-environment-variables 
* Alpaca Trade API: https://github.com/alpacahq/alpaca-trade-api-python Account Status Checking
* https://www.alphavantage.co/support/#api-key
* https://www.alphavantage.co/
* https://www.slickcharts.com/sp500
* https://en.wikipedia.org/wiki/List_of_S%26P_500_companies
* https://ipywidgets.readthedocs.io/en/stable/

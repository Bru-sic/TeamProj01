# User Journey

**Who is Claire?** "Claire" (a persona) is used to demonstrate the main features of our project. In this case, Claire is a tech savvy, amateur investor with some spare cash and an existing portfolio of shares.

**What is Claire looking for?** Claire wants to keep an eye on her portfolio to see how it is fairing and where it might be predicted to go in future, but isn’t happy with any of the tools she is currently using. Basically she wants to self-manage her portfolio. Claire finds out about our amazing python script and goes ahead with using it.   

**What is it that "Claire would love"** (but we might not have time to implement right now)? We've indicate this with comments following ***"Claire would love:"***

## Initial Setup and Configuration (once-off)
1. Firstly, Clarie needs to:
    1. Download (clone) the script and read a few important setup instructions
    1. Instal any required modules   
    1. Create accounts with our data providers   
    1. Add her trading account API keys to the script’s configuration file (.env)  
    1. Set up the composition of her current portfolio in the tool.
   
***Claire would love:*** Claire sets up and configures everything from within the script   
***Claire would love:*** Claire imports details from a file or database   

## Main Walk Through 
1. Once the setup is complete, Claire runs the tool which presents various graphs and details about her portfolio, including:
    1. current portfolio value broken down by individual security
    1. weighting in the portfolio - ***Claire would love:*** by industry sector or security type
    1. current profits and actual returns. ***Claire would love:*** annualized returns based on purchase price and purchase date compared to the latest price
    1. Comparative side by side (or on same graph) performance of each security in the portfolio (eg line graph with historical performance since purchase price cumulative returns)
    1. Variance (volatility)
    1. Covariance / correlation /  beta against a market index. ***Claire would love:*** Claire chooses the comparative index against which the comparative analysis is performed 
1.	Claire progresses with using the tool which performs forecast simulations including:
    1.  Geometric Brownian Motion (GBM) Monte Carlo simulation
    1.  Expected portfolio return at the 95% lower and upper confidence intervals
1. ***Claire would love:*** Claire is presented with advanced charting and analytics, such as some of those describe as the [Investopedia Top 7 Technical Analysis Tools](https://www.investopedia.com/top-7-technical-analysis-tools-4773275#toc-1-on-balance-volume), which includes text on how to interpret the chart / data such as:
    1. [Onbalance Volume Charts](https://www.investopedia.com/top-7-technical-analysis-tools-4773275#toc-1-on-balance-volume)
    1. [Accumulation/Distribution Line](https://www.investopedia.com/top-7-technical-analysis-tools-4773275#toc-2-accumulationdistribution-line)
1. ***Claire would love:*** Claire is presented with a dash board that she can click or hover the mouse over and see key metrics of each security in real time.
1. The tool determines the current weighting (by value) of each security in the portfolio and presents a graph and information to help Claire make any decisions about rebalancing the portfolio. ***Claire would love:*** at the press of a button the tool sends off buy and sell trade orders to automatically rebalance her  portfolio based on her weighting matrix preferences.
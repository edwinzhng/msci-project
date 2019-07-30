from datetime import datetime

import numpy as np
import pandas_datareader as pdr


# queries yahoo finance for market data of provided stocks
# returns monthly and annual return
def get_stocks(symbols):
    print("Fetching data for {}...".format(symbols))

    response = pdr.get_data_yahoo(symbols,
                                  start=datetime(2018, 6, 1),
                                  end=datetime(2019, 6, 3),
                                  interval='m')

    returns_monthly = response["Close"].pct_change().dropna()
    returns_annual = (1 + returns_monthly.mean()) ** 12 - 1
    return returns_monthly, returns_annual


# finds expected return of a 2-stock portfolio
def average_exp_return(returns_annual, weights):
    return weights[0] * returns_annual[0] + weights[1] * returns_annual[1]


# calculates variance of a 2-stock portfolio
def portfolio_variance(covariance, weights):
    return weights[0] ** 2 * covariance[0,0] + \
            weights[1] ** 2 * covariance[1,1] + \
            2 * weights[0] * weights[1] * covariance[0,1]


# returns the sharpe ratio given the necessary parameters
def sharpe_ratio(average_return, std_dev, r_f=0.02):
  return (average_return - r_f) / std_dev

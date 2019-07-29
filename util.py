import math
from datetime import datetime

import numpy as np

import pandas_datareader as pdr


# queries yahoo finance for market data of provided stock
def query(symbol):
    print("Fetching data for {}...".format(symbol))
    response = pdr.get_data_yahoo(symbol, start=datetime(2018, 6, 1), end=datetime(2019, 6, 1),interval='m')
    returns = response["Close"].pct_change().dropna()
    return returns.values


# retrieves market data for two provided stocks as an array
def get_stock_returns(stock_1_symbol, stock_2_symbol):
    stock_1_returns = query(stock_1_symbol)
    stock_2_returns = query(stock_2_symbol)
    return stock_1_returns, stock_2_returns

def annual_stock_returns(monthly_1, monthly_2):
    annual_1 = (1 + monthly_1.mean())**12 - 1
    annual_2 = (1 + monthly_2.mean())**12 - 1
    return annual_1, annual_2

# finds expected return of a stock portfolio
def average_exp_return(stock_1_returns, stock_2_returns, weight_1, weight_2):
    annual_1, annual_2 = annual_stock_returns(stock_1_returns, stock_2_returns)
    return np.average(annual_1) * weight_1 + \
            np.average(annual_2) * weight_2


# calculates variance of a 2-stock portfolio
def portfolio_variance(stock_1_returns, stock_2_returns, weight_1, weight_2):
    returns_1_annual = (1 + stock_1_returns.mean())**12 - 1
    returns_2_annual = (1 + stock_2_returns.mean())**12 - 1
    covariance = np.cov(stock_1_returns, stock_2_returns) * 12

    result = (weight_1 ** 2) * covariance[0, 0] + \
              (weight_2 ** 2) * covariance[1, 1] + \
              2 * weight_1 * weight_2 * covariance[0, 1]
    return result


# calculates standard deviation of a 2-stock portfolio
def portfolio_std_dev(stock_1_returns, stock_2_returns, weight_1, weight_2):
    var = portfolio_variance(stock_1_returns, stock_2_returns, weight_1, weight_2)
    return math.sqrt(var)

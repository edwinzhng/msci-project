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
    stock_1 = query(stock_1_symbol)
    stock_2 = query(stock_2_symbol)
    return stock_1, stock_2


# finds expected return of a stock portfolio
def average_exp_return(stock_1_returns, stock_2_returns, weight_1, weight_2):
    return np.average(stock_1_returns) * weight_1 * 10000 + \
            np.average(stock_1_returns) * weight_2 * 10000


# calculates variance of a 2-stock portfolio
def portfolio_variance(stock_1_returns, stock_2_returns, weight_1, weight_2):
    var_1 = np.var(stock_1_returns)
    var_2 = np.var(stock_2_returns)
    covariance = np.cov(stock_1_returns, stock_2_returns)[0][1]

    result = (weight_1 ** 2) * var_1 + \
              (weight_2 ** 2) * var_2 + \
              2 * weight_1 * weight_2 * covariance
    return result


def portfolio_std_dev(stock_1_returns, stock_2_returns, weight_1, weight_2):
    var = portfolio_variance(stock_1_returns, stock_2_returns, weight_1, weight_2)
    return math.sqrt(var)

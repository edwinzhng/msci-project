import math

import numpy as np

import api


# retrieves market data for two provided stocks as an array
def get_stocks(stock_1_symbol, stock_2_symbol):
    stock_1 = api.get_time_series(stock_1_symbol)
    stock_2 = api.get_time_series(stock_2_symbol)
    return stock_1, stock_2


# returns an array of stock returns
def get_returns(stock):
    returns = []
    prev_price = stock[0]
    for price in stock[1:]:
        returns.append((price / prev_price) - 1)
        prev_price = price
    return returns


# finds expected return of a stock portfolio
def average_exp_return(stock_1_returns, stock_2_returns, weight_1, weight_2):
    return np.average(stock_1_returns) * weight_1 + \
            np.average(stock_1_returns) * weight_2


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

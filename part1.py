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


# calculates variance of a 2-stock portfolio
def portfolio_variance(stock_1_returns, stock_2_returns, weight_1, weight_2):
    var_1 = np.var(stock_1_returns)
    var_2 = np.var(stock_2_returns)
    covariance = np.cov(stock_1_returns, stock_2_returns)[0][1]

    result = (weight_1 ** 2) * var_1 + \
              (weight_2 ** 2) * var_2 + \
              2 * weight_1 * weight_2 * covariance
    return result


# finds the portfolio weights with minimum variance using the step size
def min_variance_stock_weights(stock_1_returns, stock_2_returns, step=0.001):
    min_variance_weights = (0.0, 1.0)
    min_variance = float('inf')

    weight_1 = 0.0
    while weight_1 <= 1.0:
        weight_2 = 1 - weight_1
        variance = portfolio_variance(stock_1_returns, stock_2_returns,
                                      weight_1, weight_2)
        if variance < min_variance:
            min_variance_weights = (weight_1, weight_2)
            min_variance = variance

        weight_1 += step

    return min_variance, min_variance_weights


# finds expected return of a stock portfolio
def average_exp_return(stock_1_returns, stock_2_returns, weight_1, weight_2):
    return np.average(stock_1_returns) * weight_1 + \
            np.average(stock_1_returns) * weight_2


if __name__=="__main__":
    stock_1_symbol = input("Enter a stock symbol to query: ")
    stock_2_symbol = input("Enter a second stock symbol:   ")
    print("")

    stock_1, stock_2 = get_stocks(stock_1_symbol, stock_2_symbol)
    stock_1_returns = get_returns(stock_1)
    stock_2_returns = get_returns(stock_2)

    # calculate values
    var, weights = min_variance_stock_weights(stock_1_returns, stock_2_returns)
    exp_return = average_exp_return(stock_1_returns, stock_2_returns,
                                         weights[0], weights[1])

    w_1 = weights[0] * 100
    w_2 = weights[1] * 100
    std_dev = math.sqrt(var)

    print("\nResults:")
    print("    MVP proportion {0}: {1:.2f}%".format(stock_1_symbol, w_1))
    print("    MVP proportion {0}: {1:.2f}%".format(stock_2_symbol, w_2))
    print("    MVP standard deviation: {0:.2f}%".format(std_dev))
    print("    MVP expected portfolio return: {0:.2f}%".format(exp_return))

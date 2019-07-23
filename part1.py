import math

import numpy as np

import api


def get_stocks(stock_1_symbol, stock_2_symbol):
    stock_1 = api.get_time_series(stock_1_symbol)
    stock_2 = api.get_time_series(stock_2_symbol)
    return stock_1, stock_2

def portfolio_variance(stock_1, stock_2, weight_1, weight_2):
    var_1 = np.var(stock_1)
    var_2 = np.var(stock_2)
    covariance = np.cov(stock_1, stock_2)[0][1]

    result = (weight_1 ** 2) * var_1 + \
              (weight_2 ** 2) * var_2 + \
              2 * weight_1 * weight_2 * covariance
    return result

def min_variance_stock_weights(stock_1, stock_2):
    min_variance_weights = (0.0, 1.0)
    min_variance = float('inf')

    stock_1_weight = 0.0
    while stock_1_weight <= 1.0:
        stock_2_weight = 1 - stock_1_weight
        variance = portfolio_variance(stock_1, stock_2,
                                      stock_1_weight, stock_2_weight)
        if variance < min_variance:
            min_variance_weights = (stock_1_weight, stock_2_weight)
            min_variance = variance

        stock_1_weight += 0.001

    return min_variance, min_variance_weights

def expected_return(stock):
    returns_sum = 0.0

    for idx, price in enumerate(stock[1:]):
        returns_sum += (price / stock[idx - 1]) - 1

    return returns_sum / (len(stock) - 1) * 100

def average_expected_return(stock_1, stock_2, weight_1, weight_2):
    return expected_return(stock_1) * weight_1 + expected_return(stock_2) * weight_2

if __name__=="__main__":
    stock_1_symbol = input("Enter a stock symbol to query: ")
    stock_2_symbol = input("Enter a second stock symbol:   ")
    print("")

    stock_1, stock_2 = get_stocks(stock_1_symbol, stock_2_symbol)
    variance, weights = min_variance_stock_weights(stock_1, stock_2)
    std_dev = math.sqrt(variance)
    exp_return = average_expected_return(stock_1, stock_2, weights[0], weights[1])

    print("\nResults:")
    print("    MVP proportion {0}: {1:.2f}%".format(stock_1_symbol, weights[0] * 100))
    print("    MVP proportion {0}: {1:.2f}%".format(stock_2_symbol, weights[1] * 100))
    print("    MVP standard deviation: {0:.2f}%".format(std_dev))
    print("    MVP expected portfolio return: {0:.2f}%".format(exp_return))

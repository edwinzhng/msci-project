import math

import numpy as np

from util import average_exp_return, get_stock_returns, portfolio_variance


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


def run():
    stock_1_symbol = input("Enter a stock symbol to query: ")
    stock_2_symbol = input("Enter a second stock symbol:   ")
    print("")

    stock_1_returns, stock_2_returns = get_stock_returns(stock_1_symbol,
                                                         stock_2_symbol)

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


if __name__=="__main__":
    run()

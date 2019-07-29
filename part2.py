import math

import numpy as np

from util import average_exp_return, get_stock_returns, portfolio_variance


# returns the sharpe ratio given the necessary parameters
def sharpe_ratio(average_return, std_dev, r_f=0.02):
  return (average_return - r_f) / std_dev


# finds the portfolio weights with maximum sharpe ratio using the step size
def max_sharpe_ratio_stock_weights(stock_1_returns, stock_2_returns, step=0.025):
    max_sr_weights = (0.0, 1.0)
    max_sr = float('-inf')

    weight_1 = 0.0
    while weight_1 <= 1.0:
        weight_2 = 1 - weight_1

        var = portfolio_variance(stock_1_returns, stock_2_returns,
                                 weight_1, weight_2)

        expected = average_exp_return(stock_1_returns, stock_2_returns,
                                      weight_1, weight_2)

        sr = sharpe_ratio(expected, math.sqrt(var))

        if sr > max_sr:
            max_sr_weights = (weight_1, weight_2)
            max_sr = sr

        weight_1 += step

    return max_sr, max_sr_weights

# calculates return based on portfolio and risk free weights
def risk_free_market_return(stock_1_returns, stock_2_returns,
                            port_weights, risk_free_weights, r_f = 0.02):
    exp_return = average_exp_return(stock_1_returns, stock_2_returns,
                                    port_weights[0], port_weights[1])
    return exp_return * risk_free_weights[0] + r_f * risk_free_weights[1]

# calculates standard deviation based on portfolio and risk free weights
def risk_free_market_std_dev(stock_1_returns, stock_2_returns, weights, portfolio_weight):
    variance = portfolio_variance(stock_1_returns, stock_2_returns, weights[0], weights[1])
    return math.sqrt(portfolio_weight ** 2 * variance)

# case 1 calculations
def case_1(stock_1_returns, stock_2_returns, stock_1_symbol, stock_2_symbol):
    max_sharpe_ratio, weights = max_sharpe_ratio_stock_weights(stock_1_returns, stock_2_returns)

    w_1 = weights[0]
    w_2 = weights[1]

    exp_return = average_exp_return(stock_1_returns, stock_2_returns, w_1, w_2)
    variance = portfolio_variance(stock_1_returns, stock_2_returns, w_1, w_2)
    std_dev = math.sqrt(variance)

    print("\nCase 1:")
    print("    Given proportion invested in risk-free asset: 0%")
    print("    Given proportion invested in market portfolio: 100%")
    print("")
    print("    Maximum Sharpe ratio: {0:.4f}".format(max_sharpe_ratio))
    print("    Market portfolio proportion {0}: {1:.2f}%".format(stock_1_symbol, w_1 * 100))
    print("    Market portfolio proportion {0}: {1:.2f}%".format(stock_2_symbol, w_2 * 100))
    print("    Market portfolio expected return: {0:.2f}%".format(exp_return * 100))
    print("    Market portfolio standard deviation: {0:.2f}%".format(std_dev * 100))

    return weights

# case 2 calculations
def case_2(stock_1_returns, stock_2_returns, weights):
    exp_return = risk_free_market_return(stock_1_returns, stock_2_returns,
                                         weights, (0.5, 0.5))
    std_dev = risk_free_market_std_dev(stock_1_returns, stock_2_returns,
                                       weights, 0.5)

    print("\nCase 2:")
    print("    Given proportion invested in risk-free asset: 50%")
    print("    Given proportion invested in market portfolio: 50%")
    print("")
    print("    Portfolio expected return: {0:.2f}%".format(exp_return * 100))
    print("    Portfolio standard deviation: {0:.2f}%".format(std_dev * 100))


# case 3 calculations
def case_3(stock_1_returns, stock_2_returns, weights):
    exp_return = risk_free_market_return(stock_1_returns, stock_2_returns,
                                         weights, (1.5, -0.5))
    std_dev = risk_free_market_std_dev(stock_1_returns, stock_2_returns,
                                       weights, 1.5)

    print("\nCase 3:")
    print("    Given proportion invested in risk-free asset: -50%")
    print("    Given proportion invested in market portfolio: 150%")
    print("")
    print("    Portfolio expected return: {0:.2f}%".format(exp_return * 100))
    print("    Portfolio standard deviation: {0:.2f}%".format(std_dev * 100))


def run():
    stock_1_symbol = input("Enter a stock symbol to query: ")
    stock_2_symbol = input("Enter a second stock symbol:   ")
    r_f            = print("Risk-free = 2%")
    print("")

    stock_1_returns, stock_2_returns = get_stock_returns(stock_1_symbol,
                                                         stock_2_symbol)

    weights = case_1(stock_1_returns, stock_2_returns,
                     stock_1_symbol, stock_2_symbol)
    case_2(stock_1_returns, stock_2_returns, weights)
    case_3(stock_1_returns, stock_2_returns, weights)

if __name__=="__main__":
    run()

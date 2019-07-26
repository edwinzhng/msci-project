import math

import numpy as np

from util import average_exp_return, get_stock_returns


# returns the sharpe ratio given the necessary parameters
def sharpe_ratio(average_return, std_dev, r_f):
  return (average_return - r_f) / std_dev

# case 1 calculations
def case_1():
    print("\nCase 1:")
    print("    Given proportion invested in risk-free asset: 0%")
    print("    Given proportion invested in market portfolio: 100%")
    print("")
    print("    Maximum Sharpe ratio: {0:.4f}%".format(max_sharpe_ratio))
    print("    Market portfolio proportion {0}: {1:.2f}%".format(stock_1_symbol, w_1))
    print("    Market portfolio proportion {0}: {1:.2f}%".format(stock_2_symbol, w_2))
    print("    Market portfolio expected return: {0:.2f}%".format(expected_return))
    print("    Market portfolio standard deviation: {0:.2f}%".format(std_dev))


# case 2 calculations
def case_2():
    print("\nCase 2:")
    print("    Given proportion invested in risk-free asset: 50%")
    print("    Given proportion invested in market portfolio: 50%")
    print("")
    print("    Portfolio expected return: {0:.2f}%".format(expected_return))
    print("    Portfolio standard deviation: {0:.2f}%".format(std_dev))


# case 3 calculations
def case_3():
    print("\nCase 3:")
    print("    Given proportion invested in risk-free asset: -50%")
    print("    Given proportion invested in market portfolio: 100%")
    print("")
    print("    Portfolio expected return: {0:.2f}%".format(expected_return))
    print("    Portfolio standard deviation: {0:.2f}%".format(std_dev))


def run():
    stock_1_symbol = input("Enter a stock symbol to query: ")
    stock_2_symbol = input("Enter a second stock symbol:   ")
    r_f            = input("Enter a risk free rate (0 - 100): ")
    print("")

    stock_1_returns, stock_2_returns = get_stock_returns(stock_1_symbol,
                                                         stock_2_symbol)

    case_1()
    case_2()
    case_3()

if __name__=="__main__":
    run()

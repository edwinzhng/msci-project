import ast
from itertools import combinations

import numpy as np

from util import get_stocks


# calculates variance of a n-stock portfolio
def n_stock_portfolio_variance(covariances, n):
    weight = 1.0 / n
    result = 0
   
    for i in range(n):
        result +=  weight ** 2 * covariances[i, i]

    for i in range(n):
        for j in range(i + 1, n):
            result += 2 * weight ** 2 * covariances[i, j]
    
    return result


# calculates return of n-stock portfolio
def n_stock_portfolio_return(returns_annual, n):
    weight = 1.0 / n
    result = 0
    for annual_return in returns_annual:
        result += weight * annual_return
    return result


def run():
    symbols = ['ITUB', 'SLP', 'LLY', 'PSA', 'WINA', 'KRYAF', 'DIS']
    N = len(symbols)

    returns_monthly, returns_annual = get_stocks(symbols) 

    monthly = returns_monthly[symbols]
    annual = np.array(returns_annual[symbols])

    covariance = np.array(monthly.cov() * 12)

    exp_return = n_stock_portfolio_return(annual, N)
    var = n_stock_portfolio_variance(covariance, N)
    std_dev = np.sqrt(var)

    print("\nStock portfolio satisfying constraints with {} stocks:".format(N))
    print("    Stocks: {}".format(symbols))
    print("    Portfolio expected return: {0:.2f}%".format(exp_return * 100))
    print("    Portfolio standard deviation: {0:.2f}%".format(std_dev * 100))


# iterates through all combinations of stocks to find valid portfolios
def find_portfolios():
    test_symbols = ['ITUB', 'SLP', 'LLY', 'PSA', 'WINA', 'KRYAF', 'DIS', 'NVS', 'CME', 'GOLD', 'WMT']
    returns_monthly, returns_annual = get_stocks(test_symbols)
    f = open('portfolios.txt', 'w')

    for N in range(5, 11):
        for c in combinations(test_symbols, N):
            symbols = np.array(c)
            monthly = returns_monthly[symbols]
            annual = np.array(returns_annual[symbols])

            covariance = np.array(monthly.cov() * 12)

            exp_return = n_stock_portfolio_return(annual, N)
            var = n_stock_portfolio_variance(covariance, N)
            std_dev = np.sqrt(var)
        
            if std_dev <= 0.05 and exp_return >= 0.1:
                f.write('Stocks: {}, Std Dev: {}, Return: {}\n'.format(symbols, std_dev, exp_return))
            print('Stocks: {}, Std Dev: {}, Return: {}'.format(symbols, std_dev, exp_return))

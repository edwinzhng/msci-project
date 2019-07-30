import numpy as np

from util import (average_exp_return, get_stocks, portfolio_variance,
                  sharpe_ratio)


# finds the portfolio weights with maximum sharpe ratio using the step size
def max_sharpe_ratio_weights(returns_monthly, returns_annual, step=0.0001):
    max_sr_weights = [0.0, 1.0]
    max_sr = float('-inf')

    covariance = np.array(returns_monthly.cov() * 12)
    returns = np.array(returns_annual)

    weight_1 = 0.0
    while weight_1 <= 1.0:
        weight_2 = 1 - weight_1
        expected = average_exp_return(returns, [weight_1, weight_2])
        variance = portfolio_variance(covariance, [weight_1, weight_2])
        sr = sharpe_ratio(expected, np.sqrt(variance))

        if sr > max_sr:
            max_sr_weights = [weight_1, weight_2]
            max_sr = sr

        weight_1 += step

    return max_sr, max_sr_weights

# calculates return based on portfolio and risk free weights
def risk_free_market_return(returns_annual, port_weights, rf_weights, r_f = 0.02):
    exp_return = average_exp_return(np.array(returns_annual), port_weights)
    return exp_return * rf_weights[0] + r_f * rf_weights[1]

# calculates standard deviation based on portfolio and risk free weights
def risk_free_market_std_dev(returns_monthly, weights, portfolio_weight):
    covariance = np.array(returns_monthly.cov() * 12)
    variance = portfolio_variance(covariance, weights)
    return np.sqrt(portfolio_weight ** 2 * variance)

# case 1 calculations
def case_1(returns_monthly, returns_annual, symbols):
    sharpe_ratio, weights = max_sharpe_ratio_weights(returns_monthly, returns_annual)

    w_1 = weights[0]
    w_2 = weights[1]

    exp_return = average_exp_return(np.array(returns_annual), weights)
    variance = portfolio_variance(np.array(returns_monthly.cov() * 12), weights)
    std_dev = np.sqrt(variance)

    print("\nCase 1:")
    print("    Given proportion invested in risk-free asset: 0%")
    print("    Given proportion invested in market portfolio: 100%\n")
    print("    Maximum Sharpe ratio: {0:.4f}".format(sharpe_ratio))
    print("    Market portfolio proportion {0}: {1:.2f}%".format(symbols[0], w_1 * 100))
    print("    Market portfolio proportion {0}: {1:.2f}%".format(symbols[1], w_2 * 100))
    print("    Market portfolio expected return: {0:.2f}%".format(exp_return * 100))
    print("    Market portfolio standard deviation: {0:.2f}%".format(std_dev * 100))

    return weights

# case 2 calculations
def case_2(returns_monthly, returns_annual, weights):
    exp_return = risk_free_market_return(returns_annual, weights, (0.5, 0.5))
    std_dev = risk_free_market_std_dev(returns_monthly, weights, 0.5)

    print("\nCase 2:")
    print("    Given proportion invested in risk-free asset: 50%")
    print("    Given proportion invested in market portfolio: 50%\n")
    print("    Portfolio expected return: {0:.2f}%".format(exp_return * 100))
    print("    Portfolio standard deviation: {0:.2f}%".format(std_dev * 100))


# case 3 calculations
def case_3(returns_monthly, returns_annual, weights):
    exp_return = risk_free_market_return(returns_annual, weights, (1.5, -0.5))
    std_dev = risk_free_market_std_dev(returns_monthly, weights, 1.5)

    print("\nCase 3:")
    print("    Given proportion invested in risk-free asset: -50%")
    print("    Given proportion invested in market portfolio: 150%\n")
    print("    Portfolio expected return: {0:.2f}%".format(exp_return * 100))
    print("    Portfolio standard deviation: {0:.2f}%".format(std_dev * 100))


def run(returns_monthly, returns_annual, symbols):
    weights = case_1(returns_monthly, returns_annual, symbols)
    case_2(returns_monthly, returns_annual, weights)
    case_3(returns_monthly, returns_annual, weights)

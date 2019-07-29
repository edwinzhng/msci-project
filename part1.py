import numpy as np

from util import average_exp_return, get_stocks, portfolio_variance


# finds the portfolio weights with minimum variance using the step size
def min_variance_stock_weights(returns_monthly, returns_annual, step=0.0001):
    min_variance_weights = [0.0, 1.0]
    min_variance = float('inf')

    covariance = np.array(returns_monthly.cov() * 12)
    returns = np.array(returns_annual)

    weight_1 = 0.0
    while weight_1 <= 1.0:
        weight_2 = 1 - weight_1
        variance = portfolio_variance(covariance, [weight_1, weight_2])

        if variance < min_variance:
            min_variance_weights = (weight_1, weight_2)
            min_variance = variance

        weight_1 += step

    return min_variance, min_variance_weights


def run(returns_monthly, returns_annual, symbols):
    # calculate values
    var, weights = min_variance_stock_weights(returns_monthly, returns_annual)
    exp_return = average_exp_return(returns_annual, weights)

    w_1 = weights[0]
    w_2 = weights[1]
    std_dev = np.sqrt(var)

    print("\nResults:")
    print("    MVP proportion {0}: {1:.2f}%".format(symbols[0], w_1 * 100))
    print("    MVP proportion {0}: {1:.2f}%".format(symbols[1], w_2 * 100))
    print("    MVP expected portfolio return: {0:.4f}%".format(exp_return * 100))
    print("    MVP standard deviation: {0:.4f}%".format(std_dev * 100))

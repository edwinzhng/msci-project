import api

def sharpe_ratio(average_return, std_dev, r_f):
  return (average_return - r_f) / std_dev


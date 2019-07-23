import requests
import json
import numpy

API_URL = "https://www.alphavantage.co/query"
API_KEY = "N650W61IMJKOKG4L"

def query(symbol, function="TIME_SERIES_DAILY", interval="60min", outputsize="full"):
    print("Fetching data for {}...".format(symbol))
    params = {
        "function" : function,
        "symbol" : symbol,
        "interval" : interval,
        "outputsize" : outputsize,
        "apikey" : API_KEY
    }
    response = requests.get(API_URL, params=params)
    return response

def get_time_series(symbol, frequency="daily", interval="60min", outputsize="full"):
    fcn = "TIME_SERIES_{}".format(frequency.upper())
    response = query(symbol, fcn, interval, outputsize).json()
    times_series_dict = response["Time Series ({})".format(frequency[0].upper() + frequency[1:])]
    time_series = []

    for date, values in times_series_dict.items():
        year, month, day = [int(x) for x in date.split('-')]
        if year == 2019:
            if month < 6 or month == 6 and day == 1:
                time_series.append(float(values["4. close"]))
        elif year == 2018 and month >= 6:
            time_series.append(float(values["4. close"]))

    return numpy.array(time_series)

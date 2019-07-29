# MSCI 261 Project

## Group Members

Edwin Zhang, Bob Wei, Ayush Kapur

## Setup

1. Install dependencies with `pip install -r requirements.txt`

## Running the project

* Run with `python3 main.py` (Preferably run with Python 3)

Note:

* Sometimes the pandas datareader will throw an error when fetching data
* This issue is documented at https://github.com/pydata/pandas-datareader/issues/640
* If the same `KeyError: 'Date'` occurs, run `main.py` again, usually it won't occur 2 times in a row

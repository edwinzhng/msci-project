# MSCI 261 Project

## Group Members

Edwin Zhang, Bob Wei, Ayush Kapur

## Setup

1. Install dependencies with `pip install -r requirements.txt`

## Running the project

* Run with `python3 main.py` (Preferably run with Python 3)
* When part 2 runs, the program will display a plot of the efficient frontier

* After the plot is closed, the bonus will run, which is a 7-stock portfolio comprised of ITUB, SLP, LLY, PSA, WINA, KRYAF, DIS
* This portfolio has a standard deviation of 4.77% and a return of 27.12%

* All data uses the 'Close' price although the bonus portfolio also satisfies the constraints with 'Adj Close'
* If you want to test the project using 'Adj Close', you can modify the `get_stocks()` function in `util.py`

Note:

* Sometimes the pandas datareader will throw a `KeyError: 'Date'` when fetching data
* This issue is documented at https://github.com/pydata/pandas-datareader/issues/640
* If the error occurs, run `main.py` again, usually it won't occur 2 times in a row

import part1
import part2
import bonus

from util import get_stocks

if __name__=="__main__":
  print("MSCI 261 Final Project\n")
  symbols = []
  symbols.append(input("Enter a stock symbol to query: "))
  symbols.append(input("Enter a second stock symbol:   "))
  print("Risk-free = 2%\n")

  returns_monthly, returns_annual = get_stocks(symbols)

  print("\n---------- Part 1 ----------")
  part1.run(returns_monthly, returns_annual, symbols)
  print("\n---------- Part 2 ----------")
  part2.run(returns_monthly, returns_annual, symbols)
  print("\n---------- Bonus ----------\n")
  bonus.run()

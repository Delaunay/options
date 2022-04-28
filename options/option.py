from dataclasses import dataclass

import matplotlib.pyplot as plt
import pandas as pd

# %matplotlib inline

Call = 0
Put = 1

Buy = 1
Sell = -1


@dataclass
class Option:
    strike: float
    callput: float
    buysell: bool
    price: float = None
    qty: float = 100

    def __repr__(self):
        name = "Call" if self.call else "Put"

        args = [
            f"{self.strike:.2f}",
            "Buy" if self.buy else "Sell",
        ]

        if self.price:
            args.append(f"{self.price:.2f}")

        args = ", ".join(args)
        return f"{name}({args})"

    @property
    def sell(self):
        return self.buysell == Sell

    @property
    def buy(self):
        return self.buysell == Buy

    @property
    def put(self):
        return self.callput == Put

    @property
    def call(self):
        return self.callput == Call

    def payoff(self, price):
        if self.call:
            return self.buysell * max(price - self.strike, 0)

        if self.put:
            return self.buysell * max(self.strike - price, 0)

    def profit(self, price):
        return self.payoff(price) + self.cost()

    def _prices(self, spread):
        return [
            self.strike / spread,
            self.strike,
            self.strike * spread,
        ]

    def cost(self):
        return -self.buysell * self.price

    def show(self, spread=1.12):
        strikes = self._prices(spread)
        plt.plot(strikes, [self.payoff(k) for k in strikes])


class Strategy:
    def __init__(self, *options) -> None:
        self.options = options

    def payoff(self, price):
        return sum([opt.payoff(price) for opt in self.options])

    def profit(self, price):
        return sum([opt.profit(price) for opt in self.options])

    @staticmethod
    def guess_plot_spread(options):
        avg = sum([opt.strike for opt in options]) / len(options)
        return max([opt.strike / avg for opt in options])

    @staticmethod
    def generate_plot_prices(options, spread):
        prices = []
        for opt in options:
            prices.append(opt.strike)
        prices.sort()

        prices.insert(0, int(prices[0] / spread))
        prices.append(int(prices[-1] * spread))
        return prices

    def display(self, spread=None, profit=True):
        # Guess a nice spread given the price of every strike
        if spread is None:
            spread = Strategy.guess_plot_spread(self.options)

        prices = Strategy.generate_plot_prices(self.options, spread)
        cost = sum([opt.cost() for opt in self.options])

        payoffs = []
        profits = []
        for price in prices:
            payoffs.append(self.payoff(price))
            profits.append(self.profit(price))

        print(f"Cost {cost:.2f}")
        y = profits if profit else payoffs
        plt.plot(prices, y)
        return pd.DataFrame(dict(prices=prices, payoff=payoffs, profit=profits))

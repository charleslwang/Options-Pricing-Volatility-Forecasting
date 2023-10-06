# Implementing the Black-Scholes-Merton option pricing model.

import math
from scipy.stats import norm


def calculate_option_price(S, K, T, r, sigma, option_type):
    """
    Calculate the Black-Scholes-Merton option price.

    Parameters:
    - S: Current stock price (spot price)
    - K: Strike price
    - T: Time to expiration (in years)
    - r: Risk-free interest rate (annual)
    - sigma: Volatility of the underlying stock (annual)
    - option_type: 'call' for call option, 'put' for put option

    Returns:
    - Option price
    """

    if option_type not in ['call', 'put']:
        raise ValueError("Invalid option type. Must be either call or put.")

    d1 = (math.log(S / K) + (r + (sigma ** 2) / 2) * T) / (sigma * math.sqrt(T))
    d2 = d1 - sigma * math.sqrt(T)

    if option_type == 'call':
        option_price = S * norm.cdf(d1) - K * math.exp(-r * T) * norm.cdf(d2)
    else:
        option_price = K * math.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)

    return option_price


def calculate_delta(S, K, T, r, sigma, option_type):
    if option_type not in ['call', 'put']:
        raise ValueError("Invalid option type. Must be either call or put.")

    d1 = (math.log(S / K) + (r + (sigma ** 2) / 2) * T) / (sigma * math.sqrt(T))

    if option_type == 'call':
        delta = norm.cdf(d1)
    else:
        delta = -norm.cdf(-d1)

    return delta

import sys


def candy_price(weight, price):
    total_price = round(weight * price, 0)
    return total_price

print candy_price(float(sys.argv[1]), int(sys.argv[2]))
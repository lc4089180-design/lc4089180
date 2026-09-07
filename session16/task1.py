#Write a Python function check_cart_total that takes a list of item prices and returns the total. If any item price is negative, raise a ValueError with the message 'Invalid price in cart'.
def check_cart_total(prices):
    total = 0

    for price in prices:
        if price < 0:
            raise ValueError("Invalid price in cart")
        total += price

    return total


prices = [199, 299, 499]

try:
    print("Total cart amount:", check_cart_total(prices))
except ValueError as e:
    print(e)

#Testing negative price:

prices = [199, -50, 499]

try:
    print("Total cart amount:", check_cart_total(prices))
except ValueError as e:
    print(e)
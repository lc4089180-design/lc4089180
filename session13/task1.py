#Write a Python function called calculate_discounted_price that takes two arguments: price and discount_percent, and returns the final price after applying the discount.
def calculate_discounted_price(price, discount_percent):
    discount = price * discount_percent / 100
    final_price = price - discount
    return final_price


price = 999
discount_percent = 20

result = calculate_discounted_price(price, discount_percent)

print("Final price:", result)
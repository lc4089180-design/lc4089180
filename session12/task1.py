#Write a Python function called get_total_price that takes two arguments: price and quantity, and returns the total amount (price multiplied by quantity). Call this function with price=299 and quantity=3, and print the result.
def get_total_price(price, quantity):
    return price * quantity


result = get_total_price(299, 3)

print("Total price:", result)
#Build a function called get_discounted_price that takes the original price and a discount percentage, and returns the final price after applying the discount. Use this to calculate the final price for an item costing 999 with a 20% discount.
def get_discounted_price(original_price, discount_percentage):
    discount = original_price * discount_percentage / 100
    final_price = original_price - discount
    return final_price


result = get_discounted_price(999, 20)

print("Final price:", result)
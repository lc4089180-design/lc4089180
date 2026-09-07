#Build a Flipkart-style discount calculator: input the original price and discount percentage, then use arithmetic operators to calculate and print the final price after discount.
original_price = float(input("Enter original price: "))
discount_percentage = float(input("Enter discount percentage: "))

discount_amount = original_price * discount_percentage / 100
final_price = original_price - discount_amount

print(f"Final Price: Rs. {final_price:.2f}")
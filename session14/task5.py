#Use ChatGPT or Copilot to help you write a list comprehension that, given a list of product names from Flipkart, returns a new list with the names in uppercase but only if the name is longer than 6 characters. Paste your prompt and the AI's suggested code along with your final working code.
#AI Suggested Code:
products = ["Laptop", "Shoes", "Smartphone", "Watch", "Headphones"]

result = [product.upper() for product in products if len(product) > 6]

print(result)

#Final Working Code:
products = ["Laptop", "Shoes", "Smartphone", "Watch", "Headphones"]

uppercase_products = [product.upper() for product in products if len(product) > 6]

print(uppercase_products)
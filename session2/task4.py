#Given the variables: product_price = '499', discount = 50 (in rupees), and is_flash_sale = 'True', convert product_price and is_flash_sale to the correct data types, then calculate and print the final price after discount.<br><br><em><strong>Hint:</strong> Use int() and bool() for type conversion.</em>
product_price = '499' 

discount = 50 

is_flash_sale = 'True'  

product_price = int(product_price) 

is_flash_sale = bool(is_flash_sale)  

final_price = product_price - discount 

print ("Product Price:", product_price) 

print ("Discount:", discount) 

print ("Flash Sale:", is_flash_sale) 

print ("Final Price:", final_price) 
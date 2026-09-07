#Given the string 'Your Zomato order ID is: ZMT12345. Enjoy your meal!', extract only the order ID (e.g., 'ZMT12345') using string slicing and indexing.
text = "Your Zomato order ID is: ZMT12345. Enjoy your meal!"

order_id = text[25:33]

print("Order ID:", order_id)
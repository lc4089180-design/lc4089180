#Build a console script that asks the user for their Flipkart wishlist count (input as a string), converts it to an integer, and prints the count in a YouTube-style format (e.g., '1.2K' for 1200, '950' for 950).<br><br><em><strong>Hint:</strong> Use int() and f-strings; handle numbers above 1000 with one decimal place and add 'K'.</em>
wishlist_count = input ("Enter your Flipkart wishlist count: ") 

wishlist_count = int(wishlist_count)  

if wishlist_count >= 1000: 

    formatted_count = f"{wishlist_count / 1000:.1f} K" 

else: 

    formatted_count = f"{wishlist_count}" 

print (f"Wishlist Count: {formatted_count}")
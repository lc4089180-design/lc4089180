#Write a function add_to_cart(cart, item) that takes a shopping cart list and an item name, adds the item to the cart, and returns the updated cart. Test it by adding 'T-shirt', 'Shoes', and 'Watch' to an empty cart and print the result.
def add_to_cart(cart, item):
    cart.append(item)
    return cart


cart = []

cart = add_to_cart(cart, "T-shirt")
cart = add_to_cart(cart, "Shoes")
cart = add_to_cart(cart, "Watch")

print(cart)
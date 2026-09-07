#Build a Product class for a Flipkart-style shopping app with attributes: product_name, price, and rating. Add a display_details() method that prints all product details in a formatted way.
class Product:
    def __init__(self, product_name, price, rating):
        self.product_name = product_name
        self.price = price
        self.rating = rating

    def display_details(self):
        print("Product Name:", self.product_name)
        print("Price: ₹", self.price)
        print("Rating:", self.rating)


product1 = Product("Samsung Galaxy", 25000, 4.5)

product1.display_details()
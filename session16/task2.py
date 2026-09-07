#Simulate a Flipkart-style product search: write a function search_products that takes a list of product names and a search term. If the search term is empty, raise an Exception with the message 'Search term required'; otherwise, return matching products.<br><br><em><strong>Hint:</strong> Use try-except to handle the exception and print a user-friendly message.</em>
def search_products(products, search_term):
    if search_term == "":
        raise Exception("Search term required")

    matching_products = []

    for product in products:
        if search_term.lower() in product.lower():
            matching_products.append(product)

    return matching_products


products = ["iPhone 15", "Samsung Galaxy", "iPhone 14", "OnePlus 12"]

try:
    result = search_products(products, "iPhone")
    print("Matching products:", result)
except Exception as e:
    print(e)

#If the search term is empty:

try:
    result = search_products(products, "")
    print(result)
except Exception as e:
    print("Error:", e)
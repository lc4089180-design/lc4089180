#Given the following JSON-style dictionary representing a Zomato order: order = {'user': 'Amit', 'items': [{'name': 'Pizza', 'qty': 2}, {'name': 'Burger', 'qty': 1}], 'total': 450}, write code to print the name and quantity of each item in the order.<br><br><em><strong>Hint:</strong> Use a for loop to iterate through the 'items' list inside the dictionary.</em>
order = {
    "user": "Amit",
    "items": [
        {"name": "Pizza", "qty": 2},
        {"name": "Burger", "qty": 1}
    ],
    "total": 450
}

for item in order["items"]:
    print("Item:", item["name"], "| Quantity:", item["qty"])
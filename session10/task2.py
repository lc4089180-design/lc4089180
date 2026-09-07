#Write a Python function get_unique_cuisines(restaurants) that takes a list of restaurant cuisines (e.g., ['Italian', 'Chinese', 'Italian', 'Mexican', 'Chinese']) and returns a set of unique cuisines like Zomato shows in its filters.
def get_unique_cuisines(restaurants):
    return set(restaurants)


cuisines = ['Italian', 'Chinese', 'Italian', 'Mexican', 'Chinese']

result = get_unique_cuisines(cuisines)

print(result)
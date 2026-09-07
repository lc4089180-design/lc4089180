#Create a Python program that saves your 5 favorite food items and their ratings (out of 5) as a JSON file named my_food_ratings.json, then loads the file and prints each item with its rating.
import json

food_ratings = {
    "Pizza": 4.5,
    "Burger": 4.0,
    "Biryani": 5.0,
    "Dosa": 4.5,
    "Pav Bhaji": 4.0
}

with open("my_food_ratings.json", "w") as file:
    json.dump(food_ratings, file, indent=4)

with open("my_food_ratings.json", "r") as file:
    loaded_ratings = json.load(file)

for food, rating in loaded_ratings.items():
    print(food, "-", rating, "/ 5")
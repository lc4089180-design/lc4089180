#task1.py
from math_helpers import add_numbers, multiply_numbers

song1_duration = 4
song2_duration = 5

song1_plays = 100
song2_plays = 200

total_duration = add_numbers(song1_duration, song2_duration)
total_plays_product = multiply_numbers(song1_plays, song2_plays)

print("Total duration:", total_duration, "minutes")
print("Product of play counts:", total_plays_product)
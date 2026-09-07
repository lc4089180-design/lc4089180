#Given a list of movie ratings (e.g., [4.5, 3.8, 5.0, 4.2]), write a function called average_rating that returns the average rating rounded to 1 decimal place. Print the result for the list above.
def average_rating(ratings):
    average = sum(ratings) / len(ratings)
    return round(average, 1)


ratings = [4.5, 3.8, 5.0, 4.2]

result = average_rating(ratings)

print("Average rating:", result)
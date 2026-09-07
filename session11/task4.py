#Write a function get_movie_rating(movies_dict, movie_name) that takes a nested dictionary of movies (with movie names as keys and each value being another dictionary with 'genre' and 'rating') and returns the rating of the given movie. Test it with a sample dictionary containing at least three movies.
def get_movie_rating(movies_dict, movie_name):
    return movies_dict[movie_name]["rating"]


movies = {
    "Jawan": {
        "genre": "Action",
        "rating": 7.5
    },
    "RRR": {
        "genre": "Action",
        "rating": 8.0
    },
    "12th Fail": {
        "genre": "Drama",
        "rating": 9.0
    }
}

print("Rating of Jawan:", get_movie_rating(movies, "Jawan"))
print("Rating of 12th Fail:", get_movie_rating(movies, "12th Fail"))
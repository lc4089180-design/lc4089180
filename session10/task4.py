#Suppose you have two sets: watched_movies = {'RRR', 'Jawan', 'KGF', 'Pathaan'} and trending_movies = {'Jawan', 'Pathaan', 'Animal', 'Salaar'}. Write code to find and print the movies you have watched that are also trending, like BookMyShow's 'Trending Now' badge.
watched_movies = {'RRR', 'Jawan', 'KGF', 'Pathaan'}
trending_movies = {'Jawan', 'Pathaan', 'Animal', 'Salaar'}

trending_watched = watched_movies.intersection(trending_movies)

print(trending_watched)
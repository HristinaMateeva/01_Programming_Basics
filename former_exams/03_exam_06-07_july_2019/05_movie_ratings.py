import sys

number_target_movies = int(input())

max_rating = 0
min_rating = sys.maxsize
movie_max_rating = " "
movie_min_rating = " "
counter_movies = 0
sum_rating = 0

for num in range(1, number_target_movies + 1):
    movie_name = input()
    rating_current_movie = float(input())
    counter_movies += 1
    sum_rating += rating_current_movie
    if rating_current_movie > max_rating:
        max_rating = rating_current_movie
        movie_max_rating = movie_name
    elif rating_current_movie < min_rating:
        min_rating = rating_current_movie
        movie_min_rating = movie_name

average = sum_rating / number_target_movies

print(f"{movie_max_rating} is with highest rating: {max_rating:.1f}")
print(f"{movie_min_rating} is with lowest rating: {min_rating:.1f}")
print(f"Average rating: {average:.1f}")

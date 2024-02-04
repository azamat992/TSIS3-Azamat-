movies = [
    {"name": "Usual Suspects", "imdb": 7.0, "category": "Thriller"},
    {"name": "Hitman", "imdb": 6.3, "category": "Action"},
    {"name": "Dark Knight", "imdb": 9.0, "category": "Adventure"},
    {"name": "The Help", "imdb": 8.0, "category": "Drama"},
    {"name": "The Choice", "imdb": 6.2, "category": "Romance"},
    {"name": "Colonia", "imdb": 7.4, "category": "Romance"},
    {"name": "Love", "imdb": 6.0, "category": "Romance"},
    {"name": "Bride Wars", "imdb": 5.4, "category": "Romance"},
    {"name": "AlphaJet", "imdb": 3.2, "category": "War"},
    {"name": "Ringing Crime", "imdb": 4.0, "category": "Crime"},
    {"name": "Joking muck", "imdb": 7.2, "category": "Comedy"},
    {"name": "What is the name", "imdb": 9.2, "category": "Suspense"},
    {"name": "Detective", "imdb": 7.0, "category": "Suspense"},
    {"name": "Exam", "imdb": 4.2, "category": "Thriller"},
    {"name": "We Two", "imdb": 7.2, "category": "Romance"},
]

#1 IMDB score is above 5.5
def is_high_score(movie):
    return movie["imdb"] > 5.5
single_movie = {
    "name": input("Enter movie name: "),
    "imdb": float(input("Enter IMDB score: ")),
    "category": input("Enter category: "),
}
print(f"Is {single_movie['name']} a high-score movie? {is_high_score(single_movie)}")

#2 Return sublist with score above 5.5
def sublist(lst):
    return [x['name'] for x in lst if x.get('imdb', 0) > 5.5]
print(sublist(movies))

#3 Return category name
def chetan(movies, category):
    return [movie['name'] for movie in movies if movie.get('category') == category]
selected_category = input("Enter a category to filter movies: ")
result = chetan(movies, selected_category)

#4 Average IMDB score of movies
def average_imdb_score(movie_list):
    if not movie_list:
        return 0.0
    return sum(movie["imdb"] for movie in movie_list) / len(movie_list)
print(f"\nAverage IMDB score of all movies: {average_imdb_score(movies):.2f}")

#5 Average IMDB of specific Category
def average_imdb_score_by_category(movies, category):
    category_movies = [movie['imdb'] for movie in movies if movie.get('category') == category]
    return sum(category_movies) / len(category_movies) if len(category_movies) > 0 else 0.0
selected_category = input("Enter a category to compute average IMDb score: ")
result = average_imdb_score_by_category(movies, selected_category)
print(f"\nAverage IMDb score of '{selected_category}' movies: {result:.2f}")

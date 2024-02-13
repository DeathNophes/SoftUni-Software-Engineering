def movie_organizer(*args):
    result = ""
    movies_dict = {}

    for movie_name, movie_genre in args:
        if movie_genre not in movies_dict.keys():
            movies_dict[movie_genre] = []

        movies_dict[movie_genre].append(movie_name)

    sorted_movies = sorted(
        movies_dict.items(),
        key=lambda x: (-len(x[1]), x[0])
    )

    for genre, movies in sorted_movies:
        result += f"{genre} - {len(movies)}\n"
        for movie in sorted(movies):
            result += f"* {movie}\n"

    return result

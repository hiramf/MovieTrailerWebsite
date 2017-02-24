import tmdbsimple as tmdb
tmdb.API_KEY = "2f0a0100b2d036942bbdfe217197689b"


def movie_search():
    keyword = raw_input("What movie are you searching for?\n")
    print("searching for..."+keyword+"\n")
    print("Here are your results:\n")
    search = tmdb.Search()
    response = search.movie(query=keyword)
    for s in search.results:
        print(s["title"],s["id"])
    tmdb_id = raw_input("\nEnter the ID for the movie you want to know more about:\n")
    movie = tmdb.Movies(tmdb_id)
    print("'movie' has been set to "+ "'" + keyword + "'"+ "(" + tmdb_id + ")")
    response = movie.info()
    print('Title: ' + movie.title)
    print('TMDB ID: ' + str(movie.id))
    print('Tagline: ' + movie.tagline)
    print('Overview: ' + movie.overview)
    print("\n")


x=1
while True:
    command = raw_input("Type 'search' to search for movies or 'break' to exit:\n")
    if command == "search":
        movie_search()
    elif command == "break":
        break
    else:
        print('error: input not recognized')
    
    
    

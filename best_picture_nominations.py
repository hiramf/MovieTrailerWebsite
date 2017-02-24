import fresh_tomatoes  # fresh_tomatoes contains the website structure
import webbrowser
# tmdbsimple is an API for retrieving information about movies
import tmdbsimple as tmdb
tmdb.API_KEY = "[your key here]"


class Movie():
    def __init__(self, movie_title, poster_url, youtube_url, tmdb_id):
        self.movie_title = movie_title
        self.poster_url = poster_url
        self.youtube_url = youtube_url
        self.tmdb_id = tmdb_id
        overview = tmdb.Movies(self.tmdb_id)
        response = overview.info()
        """
        here we use .encode('utf-8) to tell python that the overview retrieved
        from tmdbsimple is unicode text_from_web.encode('utf-8')
        """
        self.overview = overview.overview.encode('utf-8')
        
    def show_trailer(self):
        webbrowser.open(self.youtube_url)


    

# Nominations for best picture
arrival = Movie("Arrival",
                      "http://www.scified.com/u/new-arrival-movie-poster-615813.jpg",  # NOQA
                      "https://youtu.be/tFMo3UJ4B4g",
                      "329865")
        
fences = Movie("Fences",
                     "http://cdn2-www.comingsoon.net/assets/uploads/gallery/fences/fences.jpg",  # NOQA
                     "https://youtu.be/jj-ZYPVRQbc",
                     "393457")
hacksaw_ridge = Movie("Hacksaw Ridge",
                            "http://image.tmdb.org/t/p/original/iQ8nNu5paDVLYtuTzLW5lGyczxK.jpg",  # NOQA
                            "https://youtu.be/s2-1hz1juBI",
                            "324786")

hell_or_high_water = Movie("Hell or High Water",
                                 "http://www.joblo.com/posters/images/full/hell-or-high-water-poster-gallery.jpg",  # NOQA
                                 "https://youtu.be/JQoqsKoJVDw",
                                 "338766")
hidden_figures = Movie("Hidden Figures",
                             "http://cdn2-www.comingsoon.net/assets/uploads/gallery/hidden-figures/hiddenfiguresposter.jpg",  # NOQA
                             "https://youtu.be/RK8xHq6dfAo",
                             "381284")

la_la_land = Movie("La La Land",
                         "http://www.impawards.com/2016/posters/la_la_land_ver2_xxlg.jpg",  # NOQA
                         "https://youtu.be/0pdqf4P9MB8",
                         "313369")

lion = Movie("Lion",
                   "http://www.impawards.com/2016/posters/lion_xxlg.jpg",   # NOQA
                   "https://youtu.be/bWy3It8V54Q",
                   "334543")
manchester_by_the_sea = Movie("Manchester by the Sea",
                                    "https://teaser-trailer.com/wp-content/uploads/Manchester-by-the-sea-new-poster.jpg",  # NOQA
                                    "https://youtu.be/gsVoD0pTge0",
                                    "334541")
moonlight = Movie("Moonlight",
                        "http://www.joblo.com/posters/images/full/moonlight-poster-lg.jpg",  # NOQA
                        "https://youtu.be/9NJj12tJzqc",
                        "376867")


# turn the above collection of movies
# into a list to be processed by fresh_tomatoes.py
movies = [arrival,
          fences,
          hacksaw_ridge,
          hell_or_high_water,
          hidden_figures,
          la_la_land, lion,
          manchester_by_the_sea,
          moonlight,
          ]

# prints out the title of each movie with its overview from tmdb
# for movie in movies:
#   print(movie.movie_title)
#   movie.overview()
#   print('\n')

fresh_tomatoes.open_movies_page(movies)


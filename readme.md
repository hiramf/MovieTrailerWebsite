# Movie Trailer Website

**best_picture_nominations.py** creates an html document that turns class instances into tiles that display the poster image for a movie and plays the movie trailer when user clicks on the tile. Additionally, the Python shell will print out each movie's overview, obtained from [tmdb.org](https://www.themoviedb.org/) using the [tmdbsimple API](https://pypi.python.org/pypi/tmdbsimple). 

**movie_info.py** is a program that allows you to search TMDB.org for a movie and returns information about the movie you want to know move about. There is no GUI, it runs in the shell. It also requires an API Key (which I have provided).

### Purpose
This program serves to fulfill the requirements for Udacity's Course "Programming Foundations with Python." The grading rubric can be viewed [here](https://review.udacity.com/#!/rubrics/2/view). 

### Installation
My program requires the following in order to run:
- Python 2.7
- tmdbsimple 1.5.0
- best_picture_nominations.py
- fresh_tomatoes.py

How to use tmdbsimple:
*(steps 2 and 3 have already been completed for you)*
1. In command line or terminal: 
    ```sh
    pip install tmdbsimple
    ```
2. Obtain your own API Key from [tmdb.org](https://www.themoviedb.org/documentation/api) by creating a user account and requesting an API Key.
3. Add tmdbsimple to your program and add your key
    ```sh
    import tmdbsimple as tmdb
    tmdb.API_KEY = "[your key here]"
    ```
### Usage
1. Open Python 2.7 IDLE
2. Open best_picture_nominations.py in Python IDLE
3. Run module using the menu or F5
4. Movie titles and overviews will be displayed in the Python IDLE Shell
5. A new browser tab will open displaying the website
6. Click on a movie tile in order to view the trailer for that movie

If you would like to obtain the tmdb ID of a movie, or read the tagline/overview of a movie, open **movie_info.py** and follow the instructions.

### Modifications
You can add new movies by creating a new instance of the class "Movie." Make sure to add the new instance to the "movies" list at the end of the program in order for your addition to appear on the webpage. Be sure to have the following information:
- Movie Title
- A high quality jpeg image url
- The YouTube url for the trailer
- The id for the movie from TMDB.org in order to print out the overview of the movie.
```sh 
instance = Movie("movie_title", "poster_url", "youtube_url", "tmdb_id")  # NOQA
```
*Note: each argument is a string ("string")*

### Contact
Hiram Foster
[hiramfoster.co@gmail.com](mailto:hiramfoster.co@gmail.com)

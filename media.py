# checked by PEP
import webbrowser


class Movie():
    "Thia class is for saving movies info"
    def __init__(self, movie_title, movie_storyline,
                 movie_image_url, movie_trailer_url):
        self.title = movie_title  # from 12 to 15 line are instance variables
        self.storyline = movie_storyline
        self.poster_image_url = movie_image_url
        self.trailer_youtube_url = movie_trailer_url
    # define two functions to open trailer and poster image
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

    def show_poster(self):
        webbrowser.open(self.poster_image_url)

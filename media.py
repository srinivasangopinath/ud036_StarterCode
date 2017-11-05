import webbrowser

##Title
##Storyline
##Poster Image
##Trailer_youtube
##
##Youtube Video
##Reviews

class Movie():
    """This class provides a way to store movie related information"""
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]
    ##This is the Constructor that initializes the object in memory
    def __init__(self,movie_title,movie_storyline, poster_image,trailer_youtube):
        ##The following are the Instance Variables
        self.title=movie_title
        self.storyline=movie_storyline
        self.poster_image_url=poster_image
        self.trailer_youtube_url=trailer_youtube

    ## show+_trailer is the Instance Methods
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
    

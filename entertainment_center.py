# coding=utf-8
# The fresh_tomatoes.py module has a function called open_movies_page
# that takes in one argument, as a list of movies, and creates
# an HTML file that in-turn display the movies from the list.

#  In order to create the multple object from the the class Movie,
#  Need to import the python module media.py.
import fresh_tomatoes
import media

# toy_story is the object instance of the class Movie
# There are four instance variables initialized namely Title, Storyline, Poster
# and Trailer that are related to the movie Toy Story
toy_story = media.Movie(
    "Toy Story",
    "A story of a boy and his toys the come to our life",
    "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
    "https://www.youtube.com/watch?v=vwyZH85NQC4")
# print(toy_story.storyline)

# avatar is the object instance of the class Movie
# There are four instance variables initialized namely Title, Storyline, Poster
# and Trailer that are related to the movie Avatar
avatar = media.Movie(
    "Avatar",
    "A marine on an alien planet",
    "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
    "https://www.youtube.com/watch?v=LrDoWdOIYNg")
# print(avatar.storyline)
# avatar.show_trailer()

# spongebob is the object instance of the class Movie
# There are four instance variables initialized namely Title, Storyline, Poster
# and Trailer that are related to the movie Spongebob
spongebob = media.Movie(
    "The SpongeBob SquarePants",
    "American live-action animated comedy film inspired by the Nickelodeon TV",
    "https://upload.wikimedia.org/wikipedia/en/3/31/The_SpongeBob_SquarePants_Movie_poster.jpg",
    "https://www.youtube.com/watch?v=Tv8xk7BKaNM")

# print(spongebob.storyline)
# spongebob.show_trailer()

# homealone3 is the object instance of the class Movie
# There are four instance variables initialized namely Title, Storyline, Poster
# and Trailer that are related to the movie Home Alone 3
homealone3 = media.Movie(
    "Home Alone 3",
    "Home Alone 3 (stylized as HOME ALONE3) is a 1997 American family comedy",
    "https://upload.wikimedia.org/wikipedia/en/c/cc/Home_Alone_3_film.jpg",
    "https://www.youtube.com/watch?v=CK0j5OMApkw")
# print(homealone3.storyline)

# harrypotter is the object instance of the class Movie
# There are four instance variables initialized namely Title, Storyline, Poster
# and Trailer that are related to the movie Harry Potter
harrypotter = media.Movie(
    "Harry Potter and the Deathly Hallows part 2",
    "Harry Potter and the Deathly Hallows – Part 2 is a 2011fantasy film ",
    "https://upload.wikimedia.org/wikipedia/en/d/df/Harry_Potter_and_the_Deathly_Hallows_%E2%80%93_Part_2.jpg",
    "https://www.youtube.com/watch?v=5NYt1qirBWg")
# print(harrypotter.storyline)

# gandhi is the object instance of the class Movie
# There are four instance variables initialized namely Title, Storyline, Poster
# and Trailer that are related to the movie Gandhi
gandhi = media.Movie(
    "Gandhi",
    "Gandhi is a 1982 British-Indian epic biographical drama film",
    "https://upload.wikimedia.org/wikipedia/en/1/10/Gandhi-poster.png",
    "https://www.youtube.com/watch?v=WNAm4jO9t-w")

# print(gandhi.storyline)
# gandhi.show_trailer()

# The following movies holds all the above defied movie objects in a list
movies = [toy_story, avatar, spongebob, homealone3, harrypotter, gandhi]
# When the list "movies" is passed to the function open_movies_page
# in the fresh_tomatoes module, this call will generate HTML file including
# this content
#  and produce a website to show all the list movies
fresh_tomatoes.open_movies_page(movies)
# print(media.Movie.VALID_RATINGS)
# print(media.Movie.__doc__)
# print(media.Movie.__name__)
# print(media.Movie.__module__)

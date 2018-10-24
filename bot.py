import json
from urllib.request import Request
from imdb import IMDb
import praw

ia = IMDb()
reddit = praw.Reddit(
        client_id="",
        client_secret="",
        user_agent=""
        )

with open("movies.txt", "r") as movies:
    for movie in movies:
        title = movie.rstrip("\n")
        print(ia.search_movie(title))



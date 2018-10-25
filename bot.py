import json
from urllib.request import Request
from imdb import IMDb
import praw
import configparser

ia = IMDb()
config = configparser.ConfigParser()
config.read('config.ini')

reddit = praw.Reddit(
        client_id=config['reddit']['client_id'],
        client_secret=config['reddit']['client_secret'],
        user_agent=config['reddit']['user_agent'],
        username=config['reddit']['username'],
        password=config['reddit']['password']
        )

with open("movies.txt", "r") as movies:
    for movie in movies:
        title = movie.rstrip("\n")
        print(ia.search_movie(title))

print(reddit.read_only)

for submission in reddit.subreddit('christmashorror').hot(limit=10):
    print(submission.title)

reddit.subreddit('christmashorror').submit("test2", "this is also a test submission")

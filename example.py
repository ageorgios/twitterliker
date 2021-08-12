import tweepy
import time
from accesskeys import *
from twitterbot import TwitterBot


# Twitter restricts number of bot activites by 1000 per day as of now.
number_of_iterations = 50

# Your query to search and like the tweets.
search_query = '#hello'

# The API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_SECRET
# can be accessed from https://developer.twitter.com/en/apps

bot = TwitterBot(number_of_iterations, API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_SECRET)

# Followback all your followers if you are not already following them
# bot.follow_followers()

# Like 100 tweets from the provided query
bot.like_tweets(search_query)

# bot.follow_from_tweets(search_query)

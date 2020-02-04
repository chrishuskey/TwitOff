"""
Retrieve tweets, get embeddings, and save into our DB.
"""

import basilica
import tweepy
from decouple import config
from .models import DB, Tweet, User


# Twitter authentication keys:
TWITTER_AUTH = tweepy.OAuthHandler(config('TWITTER_CONSUMER_API_KEY'),
                                   config('TWITTER_CONSUMER_API_SECRET'))
TWITTER_AUTH.set_access_token(config('TWITTER_ACCESS_TOKEN'),
                              config('TWITTER_ACCESS_TOKEN_SECRET'))
# Twitter API instance as TWITTER for easy reference:
TWITTER = tweepy.API(TWITTER_AUTH)

# Basilica connection as BASILICA:
BASILICA = basilica.Connection(config('BASILICA_API_KEY'))

# To do: Add functions later

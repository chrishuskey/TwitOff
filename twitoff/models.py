"""
The models and data infrastructure for our Twitoff flask app.
"""

from flask-sqlalchemy import SQLAlchemy

# Create our DB as a SQLAlchemy DB:
DB = SQLAlchemy()

class User(DB.Model):
    """The Twitter users that we analyze."""
    id = DB.Column(DB.BigInteger, primary_key=True)
    name = DB.Column(DB.String(15), nullable=False)

class Tweet(DB.Model):
    """The Tweets we pull from our selected users."""
    id = DB.Column(DB.BigInteger, primary_key=True)
    text = DB.Column(DB.Unicode(280))

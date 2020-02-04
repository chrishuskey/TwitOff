"""
The models and data infrastructure for our Twitoff flask app.
"""

from flask_sqlalchemy import SQLAlchemy


# Create our DB as a SQLAlchemy DB:
DB = SQLAlchemy()

class User(DB.Model):
    """The Twitter users that we analyze."""
    id = DB.Column(DB.BigInteger, primary_key=True)
    name = DB.Column(DB.String(15), nullable=False)
    newest_tweet_id = DB.Column(DB.BigInteger)
    # Representation of a User object: format to return the user object
    # as: e.g., User realdonaldtrump:
    def __repr__(self):
        return '<User {}>'.format(self.name)

class Tweet(DB.Model):
    """The Tweets we pull from our selected users."""
    id = DB.Column(DB.BigInteger, primary_key=True)
    text = DB.Column(DB.Unicode(280), nullable=False)
    # ^^ Unicode allows text, symbols, etc.
    # Add a user_id column connecting the tweet to the user who tweeted it:
    user_id = DB.Column(DB.BigInteger, DB.ForeignKey("user.id"), nullable=False)
    # Alias "user" = the User table in the DB, so we can ref. the alias below
    # (DB.backref("tweets") also adds a column "tweets" to the User table with
    # that user's tweets):
    user = DB.relationship("User", backref=DB.backref("tweets", lazy=True))
    # Column for word embeddings data as SQLAlchemy's PickleType (pickled data):
    embedding = DB.Column(DB.PickleType, nullable=False)
    # Representation of a Tweet object: format to return the tweet
    # object as: e.g., Tweet Something ridiculous.
    def __repr__(self):
        return '<Tweet {}>'.format(self.text)

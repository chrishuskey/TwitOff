"""
Entry point for Twitoff.
"""

# From this directory (.) in the file name app (app) (so .app together),
# import the create_app function:
from .app import create_app

APP = create_app()

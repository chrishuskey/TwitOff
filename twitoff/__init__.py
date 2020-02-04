"""
Entry point for our Twitoff flask app.
"""

# From this directory (.) in the file name app (app) (so .app together),
# import the create_app function:
from .app import create_app

APP = create_app()

# [?? Where does this go, and what is it for? ??]
# if __name__ == "__main__":
#     app.run(debug=True, port=8080)

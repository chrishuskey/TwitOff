from decouple import config
from flask import Flask, render_template
from .models import DB, User, Tweet  # imports our DB from models.py

# Make our "app factory" (app-creator) function:
def create_app():
    """
    Create and configure an instance of the Flask application.
    """

    app = Flask(__name__)

    # Add config. for our DB, using the URL we defined for the DB
    # as a global variable for this project (in our .env file):
    app.config['SQLALCHEMY_DATABASE_URI'] = config('DATABASE_URL')

    # Stop tracking modifications on sqlalchemy config, as per this
    # warning we are getting: 'SQLALCHEMY_TRACK_MODIFICATIONS adds
    # significant overhead and ':
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Tell our DB about the app (initialize our DB with our app):
    DB.init_app(app)

    @app.route('/')
    def root():
        # [Deployed model goes here]
        # Return in the HTML+CSS template we're using, by rendering
        # the result within the template, and returning that:
        users = User.query.all()
        return render_template("base.html",
                                title="Welcome!",
                                header="Welcome to TwitOff!",
                                text="Coming soon...",
                                users=users
                                )

    # Route at /resetdb that clears and resets our database:
    @app.route('/resetdb')
    def resetdb():
        DB.drop_all()
        DB.create_all()
        return render_template("base.html",
                               title="Reset Database",
                               users=[])

    return app

# While debugging:
# if __name__ == "__main__":
#     app.run(debug=True, port=8080)

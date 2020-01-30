from flask import Flask, render_template
from .models import DB, User, Tweet  # imports our DB from models.py

# Make our "app factory" (app-creator) function:
def create_app():
    """
    Create and configure an instance of the Flask application.
    """

    app = Flask(__name__)

    # Add config. for our DB:
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'

    # Tell our DB about the app (initialize our DB with our app):
    DB.init_app(app)

    @app.route('/')
    def root():
        # Deployed model goes here:
        return render_template("base.html",
                                title="Welcome!",
                                header="Welcome to TwitOff!",
                                text="Coming soon..."
                                )

    return app

# [?? Where does this go, and what is it for? ??]
# if __name__ == "__main__":
#     app.run(debug=True, port=8080)

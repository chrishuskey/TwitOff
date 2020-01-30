from flask import Flask

def create_app():
    """
    Create and configure an instance of the Flask application.
    """

    app = Flask(__name__)

    @app.route('/')
    def root():
        # Deployed model goes here:
        return "<h1>Hello, TwitOff!</h1>"

    return app

# [?? Where does this go, and what is it for? ??]
# if __name__ == "__main__":
#     app.run(debug=True, port=8080)

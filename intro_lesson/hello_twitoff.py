"""
Minimal Flask app for learning/practice purposes.
"""

from flask import Flask, render_template


# Make the application:
app = Flask(__name__)

# Make the route:
@app.route("/")

# Now define a function:
def hello():
    # Deployed model goes here:
    return "<h1>Hello, Twitoff!</h1>"

# -------------------------------------

# Make a second route:
@app.route("/about")

# Now make the function that goes with /about:
# render_template automatically finds a directory names "templates"
# that is next to the current .py file (this hello_twitoff.py file),
# and which holds your HTML templates.
def preds():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True, port=8080)

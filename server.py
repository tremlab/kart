import os
import bugsnag
from bugsnag.flask import handle_exceptions
from flask import (Flask, jsonify, render_template,
redirect, request, session, Markup, has_request_context)

app = Flask(__name__)
handle_exceptions(app)
app.secret_key = os.environ.get("SECRET_KEY", "somethingelse")

# Bugsnag is an error monitoring tool. This will track all server-side errors.
bugsnag.configure(
    api_key=os.environ.get("BUGSNAG_KEY", "addBugsnagKeyHere")
)

@app.route('/')
def index():
    """loads homepage"""
    return render_template("index.html")

@app.route('/suggestions ')
def suggest():
    """returns suggestions from list based on a string of the user's input so far.
    """
    return

@app.route('/kartItem')
def add_item():
    """adds user's current string input as an item to the cart.
    """
    return

@app.route('/kart')
def show_kart():
    """shows items currently in the cart with their quantity.
    """
    return

def submit_kart():
    """sends cart contents to https://kart.example.com/submit as json.
    """
    return

if __name__ == '__main__':
    # below simply confirms a page laod occurred.
    bugsnag.notify(Exception("kart: page load"))

    PORT = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=PORT)

import os
import bugsnag
from bugsnag.flask import handle_exceptions
from flask import (Flask, jsonify, render_template,
redirect, request, session, Markup, has_request_context)
from suggestions import suggs

app = Flask(__name__, static_folder="../static/dist", template_folder="../static")
handle_exceptions(app)
app.secret_key = os.environ.get("SECRET_KEY", "somethingelse")

# Bugsnag is an error monitoring tool. This will track all server-side errors.
bugsnag.configure(
    api_key=os.environ.get("BUGSNAG_KEY", "addBugsnagKeyHere")
)

@app.route('/', methods=['GET'])
def index():
    """loads homepage"""
    return render_template("index.html")

@app.route('/suggestions', methods=['GET'])
def suggest():
    """returns suggestions from list based on a string of the user's input so far.
    """
    user_input = request.args.get("user_input", "")
    offered_responses = []

    if user_input:
        for s in suggs:
            if s.startswith(user_input):
                offered_responses.append(s)

    return offered_responses

@app.route('/kartItem', methods=['POST'])
def add_item():
    """adds user's current string input as an item to the cart.
    """
    user_input = request.args.get("user_input", "")

    # add item to cart
    # empty input field

    return

@app.route('/kart', methods=['GET'])
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

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

# starting simple for troubleshooting - to hold added cart items.
current_cart = [{
    "item": "testingdfkg",
    "quantity": 42
}]

@app.route('/', methods=['GET'])
def index():
    """loads homepage"""
    return render_template("index.html")

@app.route('/suggestions', methods=['GET'])
def suggest():
    """returns suggestions from list based on a string of the user's input so far.
    """
    user_input = request.args.get("userInput", "")
    offered_responses = []

    if user_input:
        for s in suggs:
            if s.startswith(user_input):
                offered_responses.append(s)

    return jsonify(offered_responses)

@app.route('/kartItem', methods=['POST'])
def add_item():
    """adds user's current string input as an item to the cart.
    """
    # had some difficulty parsing the jquery data
    x = request.form
    y = x.to_dict(flat=False)
    user_input = y["userInput"][0]

    found = False
    for i in current_cart:
        if i["item"] == user_input:
            i["quantity"] = i["quantity"] + 1
            found = True
            break

    if found == False:
        current_cart.append({
        "item": user_input,
        "quantity": 1
        })

    # return the updated cart which will be used to update state
    return get_kart()

@app.route('/kart', methods=['GET'])
def shows_cart():
    return get_kart()

def get_kart():
    """shows items currently in the cart with their quantity.
    """
    return jsonify(current_cart)


def submit_kart():
    """sends cart contents to https://kart.example.com/submit as json.
    """

    return

if __name__ == '__main__':
    # below simply confirms a page laod occurred.
    bugsnag.notify(Exception("kart: page load"))

    PORT = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=PORT)

import os
import bugsnag
from bugsnag.flask import handle_exceptions
from flask import (Flask, jsonify, render_template,
redirect, request, session, Markup, has_request_context)
import requests
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
    if "my_kart" in session:
        print("found", session["my_kart"])
    else:
        session['my_kart'] = []

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

    for i in session["my_kart"]:
        if i["item"] == user_input:
            i["quantity"] = i["quantity"] + 1
            session.modified = True
            found = True
            break

    if found == False:
        session["my_kart"].append({
        "item": user_input,
        "quantity": 1
        })
        session.modified = True

        suggs.append(user_input)

    # return the updated cart which will be used to update state
    return get_kart()

@app.route('/kart', methods=['GET'])
def shows_cart():
    return get_kart()

def get_kart():
    """shows items currently in the cart with their quantity.
    """
    return jsonify(session["my_kart"])


def submit_kart():
    """sends cart contents to https://kart.example.com/submit as json.
    """
    payload = {"kart": session["my_kart"]}
    r = requests.post("https://kart.example.com/submit", data=payload)
    print(r.text)
    return r.status_code

    # current error returning from this url:

        # urllib3.exceptions.MaxRetryError: HTTPSConnectionPool(host='kart.example.com', port=443): Max retries exceeded with url: /submit (Caused by NewConnectionError('<urllib3.connection.VerifiedHTTPSConnection object at 0x7f3be31cb518>: Failed to establish a new connection: [Errno -2] Name or service not known',))

if __name__ == '__main__':
    # below simply confirms a page laod occurred.
    bugsnag.notify(Exception("kart: page load"))

    PORT = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=PORT)

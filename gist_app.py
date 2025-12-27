from flask import Flask, jsonify
import requests

gist_app = Flask(__name__)

@gist_app.route('/')
def homepage():
    return jsonify({"message": "This app interacts with the public gists github api and responds to requests on /user with a list of the user's publicly available gists"}), 200

@gist_app.route('/<user>')
def get_user_public_gists(user):
    url = f"https://api.github.com/users/{user}/gists"
    try:
        response = requests.get(url)
        # If the request is successful
        if response.status_code == 200:
            public_gists = response.json()
            if public_gists:
                return jsonify(public_gists), 200
            else:
                return jsonify({"message": f"No public gists found for this user."}), 404
        elif response.status_code == 429:
            return jsonify({"error": "Rate limit exceeded. Please try again later."}), 429
        else:
            return jsonify({"error": f"User is not exist in github", "message": response.json()}), response.status_code
    except Exception as e:
        return jsonify({"error": "Oops, something went wrong on our end. Please try refreshing the page or come back later", "message": str(e)}), 500

if __name__ == '__main__':
    gist_app.run(debug=True, port=8080, host='0.0.0.0')
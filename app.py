from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Home"

@app.route("/users/<user_id>")
def users(user_id):
    user_data = {
        "user_id": user_id,
        "name": "John Doe",
        "email": "john.doe@ecample.com"
    }

    extra = request.args.get("extra")
    if extra:
        user_data["extra"] = extra
    return jsonify(user_data), 200

if __name__ == "__main__":
    app.run(debug=True)

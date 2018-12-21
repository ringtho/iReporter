from flask import Flask, jsonify, request, make_response
from api.models import Users

users_list = []
app = Flask(__name__)


@app.route("/")
def hello():
    return jsonify({"message":"Hello World"}),200

@app.route("/api/v101/users", methods=["POST"])
def create_user():
    """
    This function creates a new user
    """
    data = request.get_json()

    try:
        print(data)
        if type(data["phoneNumber"]) is not int:
            raise ValueError("phoneNumber  should be integer")
        user_details = Users(data["firstname"], data["lastname"], data["othernames"],
        data["email"], data["phoneNumber"],data["username"])

        users_list.append(user_details)
    except ValueError as e:
        print(e)
        return jsonify({"status": 400, "message":"phoneNumber should be an integer"}), 400
    return jsonify({"status":201, "data": [user_details.json_format()]}),201

@app.route("/api/v101/users", methods=["GET"])
def get_users():
    users = []
    print(users_list)

    for user in users_list:
        users.append(user.json_format())

    print(users)
    if len(users) < 1:
        return jsonify({"status":200,
        "message": "There are no users created. Thanks"})
    return jsonify({"status": 200, "data": users}), 200
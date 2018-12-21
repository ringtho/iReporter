from flask import Flask, jsonify, request, make_response
from api.models import Users, RedFlag


app = Flask(__name__)


users_list = []
redflags = []

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

@app.route("/api/v101/red-flags" ,methods=["POST"])
def add_redflag():
    data = request.get_json()
    try:
        print(data)
        if type(data["createdBy"]) is not int:
            raise ValueError("createdBy field only takes an integer")
        redflag = RedFlag(data["createdBy"], data["types"], data["location"],
        data["status"], data["images"], data["videos"], data["comment"])
        redflags.append(redflag.json_format())
    except ValueError as e:
        print(e)
        return jsonify({"status": 400, "Error": "CreatedBy should be an int"}), 400
    return jsonify({"status": 201, "data": [redflag.json_format()]}), 201

@app.route("/api/v101/red-flags", methods=["GET"])
def get_redflags():
    redflag_entry = []
    print(redflags)

    for redflag in redflags:
        redflag_entry.append(redflag)

    print(redflag_entry)
    if len(redflag_entry) < 1:
        return jsonify({"status": 200, "message":"There are no red flags created"}), 200
    return jsonify({"status": 200, "data": redflag_entry }), 200

@app.route("/api/v101/red-flags/<int:red_flag_id>" ,methods=['DELETE'])
def delete_redflag(red_flag_id):
    for redflag in redflags:
        if redflag['id'] == red_flag_id:
            redflags.remove(redflag)
            return jsonify({
            "status": 200,
            "data":[{"id": redflag['id'],"message":"red-flag record has been deleted"}]
            })
        return jsonify({"Error": "The red flag record doesnt exist"})
        
@app.route("/api/v101/red-flags/<int:red_flag_id>/comment", methods=['PATCH'])
def edit_comment(red_flag_id):
    for redflag in redflags:
        if redflag["id"] == red_flag_id:
            data = request.get_json()
            redflag['comment']=data["comment"]
            return jsonify({"status": 200,
            "data": [{"id":red_flag_id, "message": "Updated red-flag record's comment"}]})
        return jsonify ({"Error": "red-flag comment not updated"})

@app.route("/api/v101/red-flag/<int:red_flag_id>", methods=["GET"])
def get_single_redflag(red_flag_id):
    single_redflag = []
    for redflag in redflags:
        if redflag["id"] == red_flag_id:
            single_redflag.append(redflag)
        print(single_redflag)

        if len(single_redflag) < 1:
            return jsonify({"status": 200, "Error": "There are no redflags in the database"})

        return jsonify({"status": 200, "data": single_redflag}), 200

@app.route("/api/v101/red-flags/<int:red_flag_id>/location", methods=['PATCH'])
def edit_location(red_flag_id):
    for redflag in redflags:
        if redflag["id"] == red_flag_id:
            data = request.get_json()
            redflag["location"] = data["location"]
            return jsonify({"status":200, "data": [{"id": red_flag_id,
            "message": "Updated red-flag record's location"}]})
        return jsonify({"Error": "red flag location not updated"})

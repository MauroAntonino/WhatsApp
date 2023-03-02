from flask import request
from flask_cors import CORS, cross_origin
from adapters.mysql.group_adapter import GroupAdapter
from adapters.mysql.user_adapter import UserAdapter
from domain.repository.users import User
from domain.usecases.group import group

from flask import Flask
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/")
def home():
    return "Hello, Flask!"

@app.route('/group',methods = ['POST'])
def create_group():
    try:
        data = request.get_json()
        name = data["name"]
        password = data["password"]
        group_name = data["group_name"]
        description = data["description"]
        resp = group.create_group(name=name , password=password , group_name= group_name, description=description )
        return {}
    except Exception as e:
        return {"response": str(e)}

@app.route('/group_messages',methods = ['GET'])
def get_group_messages():
    data = request.get_json()
    group_name = data["group_name"]
    resp = group.get_group_messages(group_name=group_name)
    print(resp)
    return {}

@app.route('/groups',methods = ['POST'])
@cross_origin()
def get_group_user_is():
    try:
        print(request.json)
        data = request.get_json()
        name = data["name"]
        password = data["password"]
        resp = group.get_groups_user_is_in(name=name, password=password)
        return {"response": resp}
    except Exception as e:
        return {"response": str(e)}

@app.route('/group_add_user',methods = ['POST'])
def group_add_user():
    try:
        data = request.get_json()
        name = data["name"]
        password = data["password"]
        group_name = data["group_name"]
        group.add_user_in_group(name=name, password=password, group_name=group_name)
        return {}
    except Exception as e:
        return {"response": str(e)}
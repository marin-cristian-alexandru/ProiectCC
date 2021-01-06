from peewee import CharField, Model, MySQLDatabase, IntegerField
from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['JWT_SECRET_KEY'] = 'Super_Secret_JWT_KEY'
jwt = JWTManager(app)

MYSQL_DB = 'app'
MYSQL_HOST = 'db'
MYSQL_PORT = 3306
MYSQL_USER = 'root'
MYSQL_PASS = 'root'

db = MySQLDatabase(MYSQL_DB, host=MYSQL_HOST, port=MYSQL_PORT, user=MYSQL_USER, passwd=MYSQL_PASS)
db.connect()

class BaseModel(Model):
    class Meta:
        database = db


class User(BaseModel):
    class Meta:
        db_table = 'users'

    id = IntegerField()
    username = CharField()
    password = CharField()


@app.route('/login', methods=['POST'])
def login():
    content = request.get_json(silent=True)
    username = content['username']
    password = content['password']

    if not username:
        return jsonify({"msg": "Missing username parameter"}), 400
    if not password:
        return jsonify({"msg": "Missing password parameter"}), 400

    user = User.get_or_none(username=username, password=password)

    if user is None:
        return jsonify({"msg": "User not found"}), 400
        
    print(user)

    # if username != 'asd' or password != 'asd':
    #     return jsonify({"msg": "Bad username or password"}), 401
    # return jsonify(user.id), 200

    access_token = create_access_token(identity=username, expires_delta=False)
    return jsonify(access_token=access_token), 200

@app.route('/protected', methods=['GET'])
@jwt_required
def protected():
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200

if __name__ == '__main__':
    app.run(port=8014)

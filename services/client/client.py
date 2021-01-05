import requests  # for sending the request
from flask import request, jsonify, Flask
from flask_jwt_extended import JWTManager, jwt_required, get_jwt_identity


print("Acesta este un client pentru serviciul TransfermarkT")
app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'Super_Secret_JWT_KEY'
jwt = JWTManager(app)

@app.route("/sell_player", methods=['POST'])
@jwt_required
def sell_player():
    player_name = request.json['player_name']
    age = request.json['age']
    ttype = "transfer_listed"
    value = request.json['value']
    contract_l = request.json['contract_l']
    price = request.json['price']
    actual_team = request.json['actual_team']

    URL = "http://server:5000/sell_player?player_name=" + player_name + "&age=" + age + \
          "&ttype=" + ttype + "&value=" + value + "&contract_l=" + contract_l + \
          "&price=" + price + "&actual_team=" + actual_team
          
    # do the request and wait for the response
    response = requests.get(URL)
    response_msg = response.json()

    if response_msg == "":
        response_f = "Transferul dumneavoastra nu a putut fi inregistrat!\n"
    else:
        response_f = response_msg

    return jsonify(response_f), 200


@app.route("/buy_player", methods=['POST'])
def buy_player():
    player_name = request.json['player_name']
    age = request.json['age']
    actual_team = request.json['actual_team']
    ttype = request.json['ttype']
    value = request.json['value']
    wage = request.json['wage']
    contract_l = request.json['contract_l']
    price = request.json['price']
    new_team = request.json['new_team']

    URL = "http://server:5000/buy_player?player_name=" + player_name + "&age=" + age + \
          "&ttype=" + ttype + "&value=" + value + "&wage=" + wage + "&contract_l=" + contract_l + \
          "&price=" + price + "&actual_team=" + actual_team + "&new_team=" + new_team

    # do the request and wait for the response
    response = requests.get(URL)
    response_msg = response.json()

    if response_msg == "":
        response_f = "Transferul dumneavoastra nu a putut fi inregistrat!\n"
    else:
        response_f = response_msg

    return jsonify(response_f), 200


@app.route("/loan_player", methods=['POST'])
def loan_player():
    player_name = request.json['player_name']
    age = request.json['age']
    actual_team = request.json['actual_team']
    ttype = "loaned"
    value = request.json['value']
    wage_percent = request.json['wage_percent']
    contract_l = request.json['contract_l']
    new_team = request.json['new_team']

    URL = "http://server:5000/loan_player?player_name=" + player_name + "&age=" + age + \
          "&ttype=" + ttype + "&value=" + value + "&wage_percent=" + wage_percent + \
          "&contract_l=" + contract_l + "&actual_team=" + actual_team + "&new_team=" + new_team

    # do the request and wait for the response
    response = requests.get(URL)
    response_msg = response.json()

    if response_msg == "":
        response_f = "Transferul dumneavoastra nu a putut fi inregistrat!\n"
    else:
        response_f = response_msg

    return jsonify(response_f), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=7777)

print("Multumim ca ati folosit serviciul TransfermarkT pentru a va actualiza situatia sportivilor!\n")


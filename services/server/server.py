from flask import request, jsonify, Flask
from datetime import datetime
from influxdb import InfluxDBClient


def add_in_db(addable_dict, ttype):
    points = []
    json_body = {}
    tags = {}
    tags['type'] = ttype
    json_body['measurement'] = 'player_transfer'
    json_body['tags'] = tags
    json_body['time'] = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')
    fields = addable_dict
    json_body['fields'] = fields

    points.append(json_body)

    r = cliIDB.write_points(points, time_precision='s', consistency='all')
    return r


# before listening to Flask requests, the server should create the influx DB
cliIDB = InfluxDBClient(host='influxdb', port=8086)

cliIDB.create_database('TransfermarkT')
# show the databases
# print(cliIDB.get_list_database())

# switch to use the client database to insert the data
cliIDB.switch_database('TransfermarkT')

# create a retention policy for the points; never delete them
cliIDB.create_retention_policy('unlimited', 'INF', '1', shard_duration='20w')

# to drop a database
# client.drop_database('TransfermarkT')

app = Flask(__name__)


@app.route("/sell_player")
def sell_player():
    # get the URL parameters in a dictionary
    addable_dict = {}
    addable_dict['player_name'] = request.args.get('player_name')
    addable_dict['age'] = int(request.args.get('age'))
    ttype = request.args.get('ttype')
    addable_dict['value'] = int(request.args.get('value'))
    addable_dict['contract_l'] = int(request.args.get('contract_l'))
    addable_dict['price'] = int(request.args.get('price'))
    addable_dict['actual_team'] = request.args.get('actual_team')

    response = ""

    # addable_dict has all the relevant pairs to add in the database
    # add in database the message
    r = add_in_db(addable_dict, ttype)

    if r:
        response = "Transferul a fost adaugat cu succes in baza de date TransfermerkT!"

    return jsonify(response), 200


@app.route("/buy_player")
def buy_player():
    # preiau parametrii din URL
    addable_dict = {}
    addable_dict['player_name'] = request.args.get('player_name')
    addable_dict['age'] = int(request.args.get('age'))
    ttype = request.args.get('ttype')
    addable_dict['value'] = int(request.args.get('value'))
    addable_dict['wage'] = int(request.args.get('wage'))
    addable_dict['contract_l'] = int(request.args.get('contract_l'))
    addable_dict['price'] = int(request.args.get('price'))
    addable_dict['actual_team'] = request.args.get('actual_team')
    addable_dict['new_team'] = request.args.get('new_team')

    response = ""

    # addable_dict has all the relevant pairs to add in the database
    # add in database the message
    r = add_in_db(addable_dict, ttype)

    if r:
        response = "Transferul a fost adaugat cu succes in baza de date TransfermerkT"

    return jsonify(response), 200


@app.route("/loan_player")
def loan_player():
    # preiau parametrii din URL
    addable_dict = {}
    addable_dict['player_name'] = request.args.get('player_name')
    addable_dict['age'] = int(request.args.get('age'))
    ttype = request.args.get('ttype')
    addable_dict['value'] = int(request.args.get('value'))
    addable_dict['wage_percent'] = int(request.args.get('wage_percent'))
    addable_dict['contract_l'] = int(request.args.get('contract_l'))
    addable_dict['actual_team'] = request.args.get('actual_team')
    addable_dict['new_team'] = request.args.get('new_team')

    response = ""

    # addable_dict has all the relevant pairs to add in the database
    # add in database the message
    r = add_in_db(addable_dict, ttype)

    if r:
        response = "Transferul a fost adaugat cu succes in baza de date TransfermerkT"

    return jsonify(response), 200


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

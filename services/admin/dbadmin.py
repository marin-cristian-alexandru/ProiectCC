from influxdb import InfluxDBClient
from flask import request, jsonify, Flask
import time

'''Alegeti unul din tipurile urmatoare:\n"
                  "transfer_listed = jucator plasat spre vanzare\n"
                  "rumour = zvon de transfer\n"
                  "confirmed = transfer acceptat de ambele parti\n"
                  "loaned = imprumut de jucator\n: '''


time.sleep(15)

# before listening to Flask requests, the server should create the influx DB
cliIDB = InfluxDBClient(host='influxdb', port=8086)

# show the databases
# print(cliIDB.get_list_database())

# switch to use the client database to insert the data
cliIDB.switch_database('TransfermarkT')

# to drop a database
# client.drop_database('TransfermarkT')


app = Flask(__name__)

@app.route("/show_type")
def show_type():
    ttype = request.args.get('ttype')
    response = []
    results = cliIDB.query('SELECT * FROM "TransfermarkT"."autogen"."player_transfer"')
    points = results.get_points(tags={'type': ttype})
    for p in points:
        response.append(p)

    return jsonify(response), 200


@app.route("/delete_type")
def delete_type():
    ttype = request.args.get('ttype')
    cliIDB.delete_series(database='TransfermarkT', measurement='player_transfer', tags={'type': ttype})
    response = ("Toate tranferurile de tipul %s au fost anulate.\n"
          "Puteti verifica listand toate tranferurile sau celelalte tipuri." % ttype)

    return jsonify(response), 200


@app.route("/show_database")
def show_database():
    response = []
    results = cliIDB.query('SELECT * FROM "TransfermarkT"."autogen"."player_transfer"')
    points = results.get_points()
    for p in points:
        response.append(p)

    return jsonify(response), 200


@app.route("/drop_transfers")
def drop_transfers():
    cliIDB.delete_series(database='TransfermarkT', measurement='player_transfer')
    response = ("Toate transferurile au fost anulate.\n"
          "Puteti folosi optiunea de listare a transferurilor pentru a verifica.")

    return jsonify(response), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=4444)

print("JUST FIFA STUFF")


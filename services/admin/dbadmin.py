from influxdb import InfluxDBClient


def show_type():
    ttype = input("Alegeti unul din tipurile urmatoare:\n"
                  "transfer_listed = jucator plasat spre vanzare\n"
                  "rumour = zvon de transfer\n"
                  "confirmed = transfer acceptat de ambele parti\n"
                  "loaned = imprumut de jucator\n: ")
    results = cliIDB.query('SELECT * FROM "TransfermarkT"."autogen"."player_transfer"')
    points = results.get_points(tags={'type': ttype})
    for p in points:
        print(p)


def delete_type():
    ttype = input("Alegeti unul din tipurile urmatoare:\n"
                  "transfer_listed = jucator plasat spre vanzare\n"
                  "rumour = zvon de transfer\n"
                  "confirmed = transfer acceptat de ambele parti\n"
                  "loaned = imprumut de jucator\n: ")
    cliIDB.delete_series(database='TransfermarkT', measurement='player_transfer', tags={'type': ttype})
    print("Toate tranferurile de tipul %s au fost anulate.\n"
          "Puteti verifica listand toate tranferurile sau celelalte tipuri." % ttype)


def show_database():
    results = cliIDB.query('SELECT * FROM "TransfermarkT"."autogen"."player_transfer"')
    points = results.get_points()
    for p in points:
        print(p)


def drop_transfers():
    cliIDB.delete_series(database='TransfermarkT', measurement='player_transfer')
    print("Toate transferurile au fost anulate.\n"
          "Puteti folosi optiunea 3 pentru a verifica.")


adminOperations = {1: show_type, 2: delete_type, 3: show_database, 4: drop_transfers}

# before listening to Flask requests, the server should create the influx DB
cliIDB = InfluxDBClient(host='influxdb', port=8086)

# show the databases
# print(cliIDB.get_list_database())

# switch to use the client database to insert the data
cliIDB.switch_database('TransfermarkT')

# to drop a database
# client.drop_database('TransfermarkT')

while (True):
    input_code = int(input("\nIntroduceti unul din urmatoarele coduri pentru operatia pe care o doriti:\n"
                           "0 - iesire interfata de administrator\n"
                           "1 - afisare a tuturor transferurilor de un anumit tip\n"
                           "2 - stergere a tuturor transferurilor de un anumit tip\n"
                           "3 - afisare a tuturor transferurilor\n"
                           "4 - stergere a tuturor transferurilor\n"))

    if input_code == 0:
        break
    else:
        adminOperations[input_code]()

print("JUST FIFA STUFF")


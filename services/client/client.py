import requests  # for sending the request


def sell_player():
    player_name = input("Introduceti numele jucatorului pe care doriti sa-l vindeti: ")
    age = int(input("Introduceti varsta jucatorului listat pentru vanzare: "))
    ttype = "transfer_listed"
    value = int(input("Valoarea actuala (in milioane de euro) a jucatorului conform FIFA: "))
    contract_l = int(input("Introduceti cati ani de contract mai are jucatorul la clubul dumneavoastra: "))
    price = int(input("Suma de bani (in milioane de euro) pe care o doriti pentru a primi o oferta: "))
    actual_team = log_team_name

    URL = "http://server:5000/sell_player?player_name=" + player_name + "&age=" + str(age) + \
          "&ttype=" + ttype + "&value=" + str(value) + "&contract_l=" + str(contract_l) + \
          "&price=" + str(price) + "&actual_team=" + actual_team
    response = requests.get(URL)
    response_msg = response.json()

    if response_msg == "":
        print("\nTransferul dumneavoastra nu a putut fi inregistrat!\n")
    else:
        print(response_msg)


def buy_player():
    player_name = input("Introduceti numele jucatorului pe care doriti sa-l cumparati: ")
    age = int(input("Introduceti varsta jucatorului de interes: "))
    actual_team = input("Introduceti echipa la care este legitimat jucatorul in prezent: ")
    ttype = input("Tipul tranferului realizat: rumour (doar o oferta) / confirmed (deja v-ati inteles cu clubul): ")
    value = int(input("Valoarea actuala (in milioane de euro) a jucatorului conform FIFA: "))
    wage = int(input("Introduceti salariul oferit jucatorului(in mii de euro pe saptamana): "))
    contract_l = int(input("Introduceti cati ani de contract oferiti jucatorului: "))
    price = int(input("Suma de bani (in milioane de euro) pe care o oferiti: "))
    new_team = log_team_name  # bring the player to this team

    URL = "http://server:5000/buy_player?player_name=" + player_name + "&age=" + str(age) + \
          "&ttype=" + ttype + "&value=" + str(value) + "&wage=" + str(wage) + "&contract_l=" + str(contract_l) + \
          "&price=" + str(price) + "&actual_team=" + actual_team + "&new_team=" + new_team

    # do the request and wait for the response
    response = requests.get(URL)
    response_msg = response.json()

    if response_msg == "":
        print("\nTransferul dumneavoastra nu a putut fi inregistrat!\n")
    else:
        print(response_msg)


def loan_player():
    player_name = input("Introduceti numele jucatorului pe care doriti sa-l imprumutati: ")
    age = int(input("Introduceti varsta jucatorului de interes: "))
    actual_team = input("Introduceti echipa la care este legitimat jucatorul in prezent: ")
    ttype = "loaned"
    value = int(input("Valoarea actuala (in milioane de euro) a jucatorului conform FIFA: "))
    wage_percent = int(input("Introduceti numarul de procente din salariul jucatorului pe care il veti oferi: "))
    contract_l = int(input("Introduceti cati ani de contract oferiti jucatorului(1/2): "))
    new_team = log_team_name  # bring the player to this team

    URL = "http://server:5000/loan_player?player_name=" + player_name + "&age=" + str(age) + \
          "&ttype=" + ttype + "&value=" + str(value) + "&wage_percent=" + str(wage_percent) + \
          "&contract_l=" + str(contract_l) + "&actual_team=" + actual_team + "&new_team=" + new_team

    # do the request and wait for the response
    response = requests.get(URL)
    response_msg = response.json()

    if response_msg == "":
        print("\nTransferul dumneavoastra nu a putut fi inregistrat!\n")
    else:
        print(response_msg)


# mapping of client operations
clientOperations = {1: sell_player, 2: buy_player, 3: loan_player}

print("Acesta este un client pentru serviciul TransfermarkT")

log_team_name = input("\nCe club de fotbal reprezentati?\n")
print("Bine ati venit, %s! Ce transfer doriti sa raportati?" % log_team_name)

while (True):

    input_code = int(input("\nIntroduceti unul din urmatoarele coduri pentru operatia pe care o doriti:\n"
                           "0 - iesire interfata de client\n"
                           "1 - vanzare jucator\n"
                           "2 - achizitie jucator\n"
                           "3 - imprumut jucator\n"))
    if input_code == 0:
        break
    else:
        clientOperations[input_code]()

print("Multumim ca ati folosit serviciul TransfermarkT pentru a va actualiza situatia sportivilor!\n")


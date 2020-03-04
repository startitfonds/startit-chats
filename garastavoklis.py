from flask import json, jsonify
from datetime import datetime

GARASTAVOKLIS = "garastavoklis.txt"

def pieraksti_garastavokli(dati):
    # No Javascript atsūtītie JSON dati
    json_dati = dati["mood"]

    # Sākumā ielasām visus garastāvokļus masīvā no faila
    faila_esosie_garastavokli = []

    # Uzstādām karogu uz False, jo sākumā neko neesam meklējuši
    lietotajam_jau_eksiste_garastavoklis = False

    with open(GARASTAVOKLIS, "r", encoding="utf-8") as faila_rindas:
        for rinda in faila_rindas:
            ielasita_rinda_json_formata = json.loads(rinda)
            # Ja atradām lietotāju ar vārdu
            if (ielasita_rinda_json_formata["vaards"] == json_dati["vaards"]):
                # tad nomainām garastāvokli uz jauno vērtību
                ielasita_rinda_json_formata["garastavoklis"] = json_dati["garastavoklis"]
                # Uzstādām mūsu karogu uz True, jo atradām lietotāju ar vārdu
                lietotajam_jau_eksiste_garastavoklis = True
            faila_esosie_garastavokli.append(ielasita_rinda_json_formata)
    
    # Ja nebijām atraduši lietotāju ar šādu vārdu, tad ieliekam masīva beigās atsūtītos datus
    if (lietotajam_jau_eksiste_garastavoklis == False):
        faila_esosie_garastavokli.append(json_dati)

    # Pārrakstām mūsu failu no jauna ar mūsu aktuālo garastāvokļu masīvu
    with open(GARASTAVOKLIS, 'w') as file:
        for line in faila_esosie_garastavokli:
            file.write(json.dumps(line, ensure_ascii=False) + "\n")

def lasi_garastavokli():
    garastavoklis_failasaturs = []
    with open(GARASTAVOKLIS, "r", encoding="utf-8") as f:
        for rinda in f:
            garastavoklis_failasaturs.append(json.loads(rinda))
    return jsonify({"mood": garastavoklis_failasaturs})
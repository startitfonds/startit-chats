from flask import json, jsonify
from datetime import datetime

LOGFAILS = "chats.txt"
PATSK = "āēīoūaeiou"
DIVSKANI = ['ai', 'au', 'ie', 'ei', 'ui', 'iu', 'oi', 'eu', 'ou']



def lasi():
    chata_rindas = []
    with open(LOGFAILS, "r", encoding="utf-8") as f:
        for rinda in f:
            chata_rindas.append(json.loads(rinda))
    return jsonify({"chats": chata_rindas})


def pieraksti_zinju(dati):
    json_data = dati["chats"]
    json_data["laiks"] = datetime.now()
    if json_data["pupinu"]:
        json_data["zinja"] = convert_beens(json_data["zinja"])
    with open(LOGFAILS, "a", newline="", encoding="utf-8") as f:
        f.write(json.dumps(json_data, ensure_ascii=False) + "\n")


def convert_beens(txt):
    output = ""
    zilbe = ""
    index = 0
    while index < len(txt):
        zilbe = txt[index] + txt[index + 1] if index < len(txt)-1 else txt[index]
        if txt[index] in PATSK:
            if any(zilbe in s for s in DIVSKANI):
                output = output + zilbe + "p" + zilbe
                index = index + 1
            else:
                output = output + txt[index] + "p" + txt[index]
        else:
            output = output + txt[index]
        index += 1
    return output
    
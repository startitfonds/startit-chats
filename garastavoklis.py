from flask import json, jsonify
from datetime import datetime

GARASTAVOKLIS = "garastavoklis.txt"

def pieraksti_garastavokli(gStavoklis):
    json_dati = gStavoklis["mood"]
    json_dati["laiks"] = datetime.now()
    garastavoklis_failasaturs = []
    with open(GARASTAVOKLIS, "a+", encoding="utf-8") as fails:
        for saturs in fails:
            garastavoklis_failasaturs = json.loads(saturs)
            if garastavoklis_failasaturs["vaards"] == json_dati["vaards"]:
                return "Garastāvoklis šim lietotājam ir jau ievadīts"
            else:
                fails.write(json.dumps(json_dati, ensure_ascii=False) + "\n")
    fails.close()

def lasi_garastavokli():
    garastavoklis_failasaturs = []
    with open(GARASTAVOKLIS, "r", encoding="utf-8") as f:
        for rinda in f:
            garastavoklis_failasaturs.append(json.loads(rinda))
    return jsonify({"mood": rinda})
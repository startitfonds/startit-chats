from flask import json, jsonify
from datetime import datetime

LOGFAILS = "chats.txt"


def lasi():
    chata_rindas = []
    with open(LOGFAILS, "r", encoding="utf-8") as f:
        for rinda in f:
            chata_rindas.append(json.loads(rinda))
    return jsonify({"chats": chata_rindas})


def pieraksti_zinju(dati):
    json_data = dati["chats"]
    json_data["laiks"] = datetime.now()
    with open(LOGFAILS, "a", newline="", encoding="utf-8") as f:
        f.write(json.dumps(json_data, ensure_ascii=False) + "\n")

GARASTAVOKLIS = "mood.txt"

def pieraksti_mood(dati):
    json_dati = dati["mood"]
    with open(GARASTAVOKLIS, "a", newline="", encoding="utf-8") as f:
        f.write(json.dumps(json_dati, ensure_ascii=False) + "\n")

def lasi_mood():
    mood_status = []
    with open(GARASTAVOKLIS, "r", encoding="utf-8") as f:
        for row in f:
            mood_status.append(json.loads(row))
    return jsonify({"mood": row})

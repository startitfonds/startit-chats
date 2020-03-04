from flask import Flask, json, jsonify, render_template, request
import chats, garastavoklis

app = Flask('app')

@app.route('/')
def index_lapa():
  return render_template('chats.html')

@app.route('/health')
def health_check():
  return "OK"

@app.route('/chats/lasi')
def ielasit_chatu():
  return chats.lasi()

@app.route('/chats/suuti', methods=['POST'])
def suutiit_zinju():
  dati = request.json
  chats.pieraksti_zinju(dati)
  return chats.lasi()
  
@app.route('/garastavoklis/lasit_garastavokli')
def sanjemt_garastavokli():
  return garastavoklis.lasi_garastavokli() 

@app.route('/garastavoklis/pierakstit_grarastavokli', methods=['POST'])
def pierakstit_garastavokli():
  gStavoklis = request.json
  garastavoklis.pieraksti_garastavokli(gStavoklis)
  return garastavoklis.lasi_garastavokli()

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)

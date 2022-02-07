from flask import Flask, render_template, jsonify
from requests import get
import json
import os

app = Flask(__name__)
try:
    app.config.from_file('/data/options.json', json.load)
except:
    print('Could not load options file')

url = "http://supervisor/core/api/states/"
token = os.getenv('SUPERVISOR_TOKEN')

headers = {
    "Authorization": "Bearer " + token,
    "content-type": "application/json",
}

@app.route("/")
def base():
    return render_template('base.html')

@app.route("/api")
def api():
    newDict = []
    for entity_id in app.config['SENSOR_ENTITY_IDS']:
        response = get(url + entity_id, headers=headers)
        try:
            # load json response into dict
            haapi = json.loads(response.text)
            friendly_name = haapi["attributes"]["friendly_name"]
            # use .get to set blank default unit of measurement
            unit_of_measurement = haapi["attributes"].get("unit_of_measurement", "")
            newDict.append({'friendly_name': friendly_name, 'state_and_unit': haapi["state"] + " " + unit_of_measurement})
        except:
            raise Exception('Could not load json from HA API')
    return jsonify(newDict)

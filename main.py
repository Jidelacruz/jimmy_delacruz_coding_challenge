import json
import logging

import flask_expects_json
from flask import Flask, request

import Algo_compute_challenge

app = Flask(__name__)
json_schema = open("validation_schema.json")
schema = {
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "load": {
      "type": "integer"
    },
    "fuels": {
      "type": "object",
      "properties": {
        "gas(euro/MWh)": {
          "type": "number"
        },
        "kerosine(euro/MWh)": {
          "type": "number"
        },
        "co2(euro/ton)": {
          "type": "number"
        },
        "wind(%)": {
          "type": "number"
        }
      },
      "required": [
        "gas(euro/MWh)",
        "kerosine(euro/MWh)",
        "co2(euro/ton)",
        "wind(%)"
      ]
    },
    "powerplants": {
      "type": "array",
      "items": [
        {
          "type": "object",
          "properties": {
            "name": {
              "type": "string"
            },
            "type": {
              "type": "string"
            },
            "efficiency": {
              "type": "number"
            },
            "pmin": {
              "type": "number"
            },
            "pmax": {
              "type": "number"
            }
          },
          "required": [
            "name",
            "type",
            "efficiency",
            "pmin",
            "pmax"
          ]
        },
      ]
    }
  },
  "required": [
    "load",
    "fuels",
    "powerplants"
  ]
}


@app.route('/')
def hello_world():
    return 'Hey, we have Flask in a Docker container!'

@app.route('/productionplan', methods=['POST'])
#@flask_expects_json.expects_json(schema)
def production_plan():
    request_data = request.get_json()
    return Algo_compute_challenge.production_data(request_data)

if __name__ == '__main__':
    app.run(debug=True, port=8888)
#!/usr/bin/env python
# -*- coding: utf8 -*-

import json
from flask import Flask, jsonify
from flask_restful import Api, Resource, reqparse


app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('c', type=str, required=True)
parser.add_argument('v', type=float, required=True)
parser.add_argument('r', type=str, required=True)
parser.add_argument('s', type=str, required=True)
parser.add_argument('d', type=str, required=True)


@app.route('/api/v1.0/deploy', methods=['GET'])
def deploy():
    args = parser.parse_args()
    componente = args['c']
    versao = args['v']
    responsavel = args['r']
    status = args["s"]
    data = args["d"]
    print(str(versao))
    return jsonify({"versao": versao, "componente": componente, "responsavel": responsavel,
                    "status": status, "data": data})


if __name__ == '__main__':
    app.run(debug=True)

#!/usr/bin/env python
# -*- coding: utf8 -*-


from flask import Flask, jsonify
from flask_restful import reqparse
from DAO import DAO


app = Flask(__name__)

parser = reqparse.RequestParser()
parser.add_argument('c', type=str, required=True)
parser.add_argument('v', type=float, required=True)
parser.add_argument('r', type=str, required=True)
parser.add_argument('s', type=str, required=True)
parser.add_argument('d', type=str, required=True)


@app.route('/api/v1.0/deploy', methods=['GET'])
def deploy():
    args = parser.parse_args()

    ret = DAO.inserir_dados(args)
    if ret:
        return jsonify({"status": "Sucesso", "message": "Dados inseridos com sucesso!"})
    else:
        return jsonify({"status": "Erro", "code": 500, "data": None, "message": "Ocorreu um erro ao inserir as informações."})


if __name__ == '__main__':
    app.run(debug=True)

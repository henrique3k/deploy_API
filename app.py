#!/usr/bin/env python
# -*- coding: utf8 -*-


from flask import Flask, jsonify
from flask_restful import reqparse
from DAO import DAO
import logging, json
from bson import json_util


logging.basicConfig(filename='deploy_api.log', level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(funcName)s => %(message)s')


app = Flask("deploy_api")

parser = reqparse.RequestParser()
parser.add_argument('c', type=str, required=True)
parser.add_argument('v', type=float, required=True)
parser.add_argument('r', type=str, required=True)
parser.add_argument('s', type=str, required=True)


@app.route('/api/v1.0/deploy', methods=['GET'])
def deploy():
    args = parser.parse_args()

    ret, _id = DAO.inserir_dados_mongo(args)
    if ret:
        logging.info("Dados inseridos com sucesso.")
        logging.debug(args)
        return jsonify({"status": "Sucesso", "message": "Dados inseridos com sucesso!",
                        "Object_id": str(_id)})
    else:

        logging.info("Erro ao inserir os dados.")
        logging.debug(args)
        return jsonify({"status": "Erro", "code": 500, "data": None, "message": "Ocorreu um erro ao inserir as informações."})


@app.route('/api/v1.0/export', methods=['GET'])
def export():
    _ret = DAO.return_dados()

    a = json.dumps(_ret, default=json_util.default)
    return jsonify({"data": json.loads(a)})


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")

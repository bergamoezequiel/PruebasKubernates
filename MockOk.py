import sqlite3

from flask import Flask, request
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
#app.config['SERVER_NAME'] = '127.0.0.1:5555'
api = Api(app)


	
class Cliente(Resource):
	def get(self):
		usuario={"success":"yes"}
		return usuario, 200


	

api.add_resource(Cliente, "/Clientes")
if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5555")
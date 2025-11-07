from flask import Flask, jsonify
import pymysql
pymysql.install_as_MySQLdb()

from flask_cors import CORS

from config import config

app = Flask(__name__)

CORS(app)

conexion = pymysql(app)
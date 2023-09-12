import mysql.connector
import json


def get_db_config():
    with open('config.json', 'r') as f:
        config = json.load(f)
    return config['db']


def create_connection(dictionary=False):
    config = get_db_config()
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor(dictionary=dictionary)
    return cnx, cursor



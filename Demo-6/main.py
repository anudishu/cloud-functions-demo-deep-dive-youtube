import pymysql
import base64
import json
from os import getenv
from flask import Response



CONNECTION_NAME = "my-project-asksumit:us-east1:test-sql-1"
HOST = "34.139.11.217"
DB_USER = "root"
DB_PASSWORD = "}ao=|BU99|$,@rkq"
DB_NAME = "mydb"

mysql_config_for_local = {
  'host': HOST,
  'user': DB_USER,
  'password': DB_PASSWORD,
  'db': DB_NAME,
  'charset': 'utf8mb4',
  'cursorclass': pymysql.cursors.DictCursor
  }

mysql_config_for_cloud_functions = {
  'unix_socket': f'/cloudsql/{CONNECTION_NAME}',
  'user': DB_USER,
  'password': DB_PASSWORD,
  'db': DB_NAME,
  'charset': 'utf8mb4',
  'cursorclass': pymysql.cursors.DictCursor
  }

def hello(request):
    if getenv("ENVIRONMENT","local") == "cloudfunction":
        print("Running in Cloud Functions Environment")
        connection = pymysql.connect(**mysql_config_for_cloud_functions)
    else:
        print("Running on Local machine")
        connection = pymysql.connect(**mysql_config_for_local)

    with connection.cursor() as cursor:
        sql = "SELECT * from students"
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
    return Response(json.dumps(result),  mimetype='application/json')

if __name__ == "__main__":
    hello(None)

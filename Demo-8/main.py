import pymysql
import base64
import json
from os import getenv
from flask import Response




CONNECTION_NAME = "gcp-cloud-functions-demo-1:us-east1:test-sql-1"
HOST = "34.75.46.233"
DB_USER = "root"
if getenv("ENVIRONMENT","local") == "cloudfunction":
    DB_PASSWORD = getenv("DATABASE_PASSWORD")
else:
    DB_PASSWORD = "admin"
DB_NAME = "mydb"

print(f"DB Password is: {DB_PASSWORD}")

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
    if request.method == 'OPTIONS':
        # Allows GET requests from any origin with the Content-Type
        # header and caches preflight response for an 3600s
        headers = {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'GET',
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Max-Age': '3600'
        }

        return ('', 204, headers)

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
    
    headers = {
        'Access-Control-Allow-Origin': '*',
        'mimetype':'application/json'
    }

    return Response(json.dumps(result),headers=headers)

if __name__ == "__main__":
    hello(None)

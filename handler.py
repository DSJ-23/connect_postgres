import json
from sqlalchemy import create_engine
import psycopg2
from connection import username, password, endpoint, db

db_string = f"postgres://{username}:{password}@{endpoint}/{db}"
print(db_string)
# db = create_engine(db_string)

def hello(event, context):
    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "input": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response


import json
# from sqlalchemy import create_engine
# import psycopg2
# from connection import username, password, endpoint, db
# import pandas as pd
from response import *

# db_string = f"postgres://{username}:{password}@{endpoint}/{db}"
# db = create_engine(db_string)

# df = pd.DataFrame(
#     [["a", "b"], ["c", "d"]],
#     columns=["col 1", "col 2"],
# )

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

# def pandas_to_json(df):
#     df = df.to_json(orient="records")
#     df = json.loads(df)
#     return df

# def sample_pandas(event, context):
#     reponse = response_dump("200", pandas_to_json(df))
#     return reponse


# print(sample_pandas(1,3))







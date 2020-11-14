import json

def response_dump(status, body):
    return {"statusCode": status, "body": json.dumps(body)}
import json
import boto3
import os
import traceback
import uuid
from botocore.exceptions import ClientError

# import requests


def scanRescursive(ddb, **kwargs):
    response = ddb.scan(**kwargs)
    data = response.get('Items')
    while 'LastEValuatedKey' in response:
        response = kwargs.get('table').scan(ExclusiveStartKey=response['LastEvaluatedKey'], **kwargs)
        data.extend(response['Items'])
    return data
    

def lambda_handler(event, context):
    
    table_name = os.environ['TABLE']
    person_tbl = boto3.resource('dynamodb', endpoint_url="http://docker.for.mac.localhost:8000/").Table(table_name)
    try:
        if event['httpMethod'] == 'GET':
            data = scanRescursive(ddb=person_tbl)
            return {
                'statusCode': 200,
                'body': data
            }
        elif event['httpMethod'] == 'POST':
            body_dict = json.loads(event['body'])
            print(body_dict)
            p_id = str(uuid.uuid4())
            person_tbl.put_item(
                Item={
                    'Id': p_id,
                    'FirstName': body_dict['FirstName'],
                    'LastName': body_dict['LastName']
                }
            )
            print("Item inserted!")
            return {
                'statusCode': 201,
                'body': p_id
            }
    except Exception as e:
        return {'statusCode': 400, 'body': {e}}

import json
import boto3
import os
import traceback
from botocore.exceptions import ClientError

# import requests



def lambda_handler(event, context):
    
    table_name = os.environ['TABLE']
    region = 'us-east-1'
    person_tbl = boto3.resource('dynamodb', endpoint_url="http://docker.for.mac.localhost:8000/").Table(table_name)
    try:
        if event['httpMethod'] == 'GET':
            return {
                'statusCode': 200,
                'body': 'Hello from Lambda!'
            }
        else:
            body_dict = json.loads(event['body'])
            return {
                'statusCode': 200,
                'body': body_dict
            }
    except Exception as e:
        return {'statusCode': 400, 'body': {e}}

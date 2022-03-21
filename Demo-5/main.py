import functions_framework
import base64
import json

def hello(event, context):
    print(f"Context: {context}")
    print(f"Event: {event}")
    print(f"This Function was triggered by messageId {context.event_id} published at {context.timestamp} to {context.resource['name']}")
    name = "Stranger"
    if 'data' in event:
        name = base64.b64decode(event['data']).decode('utf-8')
    print('Hello, {}!'.format(name))
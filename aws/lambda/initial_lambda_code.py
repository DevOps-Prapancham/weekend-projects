import json

def lambda_handler(event, context):
  name = event['name'] if name in event else 'World'
  message = f'Hello {name}! Is this your first code to run?'
  return{
        'statusCode': 200
        'body': json.dumps({'message': message})
  }

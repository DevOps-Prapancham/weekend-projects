import json
import requests

def lambda_handler(event, context):
    response = requests.get("https://official-joke-api.appspot.com/random_joke")
    joke = response.json()
    
    return {
        'statusCode': 200,
        'body': json.dumps({
            'setup': joke['setup'],
            'punchline': joke['punchline']
        })
    }

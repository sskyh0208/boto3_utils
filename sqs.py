import json

'''
Note:
    1. Lambdaでsqsメッセージをトリガ取得する場合GetQueueAttribute, ReceiveMessage, DeleteMessageの権限が必要
'''

def get_sns_sqs_message(event: dict) -> dict:
    '''Get sns messages via sqs.
    '''
    return json.loads(event['Records'][0]['body'])

def get_sns_sqs_messages(event: dict) -> list:
    '''Get all sns messages via sqs.
    '''
    return [body['message'] for body in json.loads(event['Records'][0]['body'])]

def get_sns_message_subject(event: dict) -> str:
    '''SQS経由のSNSメッセージの件名を取得する
    '''
    message = get_sns_sqs_message(event)
    return message['Subject']

def get_sns_message_message(event: dict) -> str:
    '''SQS経由のSNSメッセージの内容を取得する
    '''
    body_message = get_sns_sqs_message(event)
    message = body_message['Message']
    try:
        return json.loads(message)
    except json.decoder.JSONDecodeError as e:
        return message
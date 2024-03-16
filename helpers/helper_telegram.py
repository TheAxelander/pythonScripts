from helpers import helper_redis
import requests


def send_message(message):
    key = 'dotnet-scripts:telegram'
    redis = helper_redis.get_redis_database()

    data = redis.hgetall(key)
    token = data['token']
    chat_id = data['chat_id']

    send_url = f'https://api.telegram.org/bot{token}/sendMessage'
    params = {'chat_id': chat_id, 'text': message}

    response = requests.post(send_url, data=params)
    return response.json()

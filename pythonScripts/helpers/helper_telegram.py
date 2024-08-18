from pythonScripts.helpers.helper_env import get_env_file_content
import requests


def send_message(message):
    token = get_env_file_content()['telegram-token']
    chat_id = get_env_file_content()['telegram-chat-id']

    send_url = f'https://api.telegram.org/bot{token}/sendMessage'
    params = {'chat_id': chat_id, 'text': message}

    response = requests.post(send_url, data=params)
    return response.json()

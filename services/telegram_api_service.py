# Telegram Variables
import requests
from dotenv import dotenv_values

# Environment Variables
ENV = dotenv_values()

telegramToken = ENV.get('TELEGRAMTOKEN')
telegramChatId = ENV.get('TELEGRAMCHATID')
telegramHostName = ENV.get('TELEGRAMHOSTNAME')

def sendMessage(message, parseMode):
    telegramUrl = f'{telegramHostName}/{telegramToken}/sendMessage?chat_id={telegramChatId}&text={message}&parse_mode={parseMode}'
    res = requests.get(telegramUrl)
    if res.status_code != 200:
        raise Exception('Error trying to send Telegram message')
    return res.json()
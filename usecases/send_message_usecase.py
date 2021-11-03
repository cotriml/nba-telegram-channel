from services import telegram_api_service
from datetime import datetime, timedelta

def sendMessage(message):
    return telegram_api_service.sendMessage(message, parseMode='html')

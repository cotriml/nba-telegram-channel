from usecases.generate_yesterdays_games_message_usecase import generateMessage
from usecases.send_message_usecase import sendMessage

try:
    message = generateMessage()
    sendMessage(message)
except Exception as e:
    errorMessage = 'Failed! ' + str(e)
    sendMessage(errorMessage)
    print(errorMessage)

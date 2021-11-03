from services import nba_api_service
from datetime import datetime, timedelta

todaysDate = datetime.today().strftime('%Y-%m-%d')

def listTodaysGames():
  return nba_api_service.getGamesByDate(todaysDate)

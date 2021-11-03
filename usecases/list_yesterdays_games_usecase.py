from services import nba_api_service
from datetime import datetime, timedelta

yesterdaysDate = (datetime.today() - timedelta(days=1)).strftime('%Y-%m-%d')

def listYesterdaysGames():
  return nba_api_service.getGamesByDate(yesterdaysDate)

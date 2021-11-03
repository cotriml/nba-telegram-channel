from services import nba_api_service

def getGameDetail(gameId):
  return nba_api_service.getGameDetail(gameId)

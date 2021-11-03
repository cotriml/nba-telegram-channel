from usecases import list_yesterdays_games_usecase, get_game_detail_usecase
import time


def generateMessage():
    res = list_yesterdays_games_usecase.listYesterdaysGames()
    games = res['api']['games']
    message = '🏀 Resultados 🏀'

    for index, game in enumerate(games):
        gameDetail = get_game_detail_usecase.getGameDetail(game['gameId'])
        vTeam = gameDetail['api']['game'][0]["vTeam"]
        hTeam = gameDetail['api']['game'][0]["hTeam"]

        message += f'\n\n\n<b>GAME {index + 1}:</b>\n'
        message += f'{vTeam["nickname"]} ({vTeam["score"]["win"]}:{vTeam["score"]["loss"]}) [{vTeam["score"]["points"]}] X '
        message += f'[{hTeam["score"]["points"]}] ({hTeam["score"]["win"]}:{hTeam["score"]["loss"]}) {hTeam["nickname"]}\n'
        message += f'{game["arena"]} ({game["city"]})\n\n'

        vTeamleaders = getLeadersPlayers(vTeam['leaders'])
        hTeamleaders = getLeadersPlayers(hTeam['leaders'])

        if bool(vTeamleaders["topPointsPlayer"]) or bool(hTeamleaders["topPointsPlayer"]):
            message += '<b>Top Pontos:</b>\n'
            if bool(vTeamleaders["topPointsPlayer"]):
                message += f'{vTeamleaders["topPointsPlayer"]["name"]}({vTeam["shortName"]}) ({vTeamleaders["topPointsPlayer"]["points"]})\n'

            if bool(hTeamleaders["topPointsPlayer"]):
                message += f'{hTeamleaders["topPointsPlayer"]["name"]}({hTeam["shortName"]}) ({hTeamleaders["topPointsPlayer"]["points"]})\n'

        if bool(vTeamleaders["topAssistsPlayer"]) or bool(hTeamleaders["topAssistsPlayer"]):
            message += '\n<b>Top Assistências:</b>\n'
            if bool(vTeamleaders["topAssistsPlayer"]):
                message += f'{vTeamleaders["topAssistsPlayer"]["name"]}({vTeam["shortName"]}) ({vTeamleaders["topAssistsPlayer"]["assists"]})\n'

            if bool(hTeamleaders["topAssistsPlayer"]):
                message += f'{hTeamleaders["topAssistsPlayer"]["name"]}({hTeam["shortName"]}) ({hTeamleaders["topAssistsPlayer"]["assists"]})\n'

        if bool(vTeamleaders["topReboundsPlayer"]) or bool(hTeamleaders["topReboundsPlayer"]):
            message += '\n<b>Top Rebotes:</b>\n'
            if bool(vTeamleaders["topReboundsPlayer"]):
                message += f'{vTeamleaders["topReboundsPlayer"]["name"]}({vTeam["shortName"]}) ({vTeamleaders["topReboundsPlayer"]["rebounds"]})\n'

            if bool(hTeamleaders["topReboundsPlayer"]):
                message += f'{hTeamleaders["topReboundsPlayer"]["name"]}({hTeam["shortName"]}) ({hTeamleaders["topReboundsPlayer"]["rebounds"]})\n'

        if bool(vTeamleaders["topBlocksPlayer"]) or bool(hTeamleaders["topBlocksPlayer"]):
            message += '\n<b>Top Tocos:</b>\n'
            if bool(vTeamleaders["topBlocksPlayer"]):
                message += f'{vTeamleaders["topBlocksPlayer"]["name"]}({vTeam["shortName"]}) ({vTeamleaders["topBlocksPlayer"]["blocks"]})\n'

            if bool(hTeamleaders["topBlocksPlayer"]):
                message += f'{hTeamleaders["topBlocksPlayer"]["name"]}({hTeam["shortName"]}) ({hTeamleaders["topBlocksPlayer"]["blocks"]})\n'

        time.sleep(15)

    return message


def getLeadersPlayers(leaders):
    assistsPlayers = []
    pointsPlayers = []
    reboundsPlayers = []
    blocksPlayers = []

    topAssistsPlayer = {}
    topPointsPlayer = {}
    topReboundsPlayer = {}
    topBlocksPlayer = {}

    for leader in leaders:
        if 'assists' in leader:
            leader['assists'] = int(leader['assists'])
            assistsPlayers.append(leader)
        elif 'points' in leader:
            leader['points'] = int(leader['points'])
            pointsPlayers.append(leader)
        elif 'rebounds' in leader:
            leader['rebounds'] = int(leader['rebounds'])
            reboundsPlayers.append(leader)
        elif 'blocks' in leader:
            leader['blocks'] = int(leader['blocks'])
            blocksPlayers.append(leader)

    if assistsPlayers:
        topAssistsPlayer = assistsPlayers[
            next((index for (index, value) in enumerate(assistsPlayers) if value["assists"] == max(
                value['assists'] for value in assistsPlayers)), StopIteration)
        ]
    if pointsPlayers:
        topPointsPlayer = pointsPlayers[
            next((index for (index, value) in enumerate(pointsPlayers) if value["points"] == max(
                value['points'] for value in pointsPlayers)), StopIteration)
        ]
    if reboundsPlayers:
        topReboundsPlayer = reboundsPlayers[
            next((index for (index, value) in enumerate(reboundsPlayers) if value["rebounds"] == max(
                value['rebounds'] for value in reboundsPlayers)), StopIteration)
        ]
    if blocksPlayers:
        topBlocksPlayer = blocksPlayers[
            next((index for (index, value) in enumerate(blocksPlayers) if value["blocks"] == max(
                value['blocks'] for value in blocksPlayers)), StopIteration)
        ]

    topLeaders = {
        'topAssistsPlayer': topAssistsPlayer,
        'topPointsPlayer': topPointsPlayer,
        'topReboundsPlayer': topReboundsPlayer,
        'topBlocksPlayer': topBlocksPlayer
    }
    return (topLeaders)

import requests
from dotenv import dotenv_values
from datetime import datetime

# Environment Variables
ENV = dotenv_values()

# NBA API Variables
rapidApiHost = ENV.get('X-RAPIDAPI-HOST')
rapidApiKey = ENV.get('X-RAPIDAPI-KEY')
rapidApiProtocol = ENV.get('X-RAPIDAPI-PROTOCOL')

configiHeaders = {
    "x-rapidapi-host": rapidApiHost,
    "x-rapidapi-key": rapidApiKey
}


def getGamesByDate(date):
    nbaApiUrl = f'{rapidApiProtocol}://{rapidApiHost}/games/date/{date}'
    res = requests.get(nbaApiUrl, headers=configiHeaders)
    if res.status_code != 200:
        raise Exception(f'Error trying to get NBA games by date: {date}')
    return res.json()


def getGameDetail(gameId):
    nbaApiUrl = f'{rapidApiProtocol}://{rapidApiHost}/gameDetails/{gameId}'
    res = requests.get(nbaApiUrl, headers=configiHeaders)
    if res.status_code != 200:
        raise Exception(f'Error trying to get NBA game detail: {gameId}')
    return res.json()


def getMockGamesByDate(date):
    res = {
        "api": {
            "status": 200,
            "message": "GET games/date/2021-10-31",
            "results": 10,
            "filters": [
                "seasonYear",
                "league",
                "gameId",
                "teamId",
                "date",
                "live"
            ],
            "games": [
                {
                    "seasonYear": "2021",
                    "league": "standard",
                    "gameId": "9648",
                    "startTimeUTC": "2021-10-31T00:00:00.000Z",
                    "endTimeUTC": "2021-10-31T02:28:00.000Z",
                    "arena": "United Center",
                    "city": "Chicago",
                    "country": "USA",
                    "clock": "",
                    "gameDuration": "2:18",
                    "currentPeriod": "4/4",
                    "halftime": "0",
                    "EndOfPeriod": "0",
                    "seasonStage": "2",
                    "statusShortGame": "3",
                    "statusGame": "Finished",
                    "vTeam": {
                        "teamId": "40",
                        "shortName": "UTA",
                        "fullName": "Utah Jazz",
                        "nickName": "Jazz",
                        "logo": "https://upload.wikimedia.org/wikipedia/fr/3/3b/Jazz_de_l%27Utah_logo.png",
                        "score": {
                            "points": "99"
                        }
                    },
                    "hTeam": {
                        "teamId": "6",
                        "shortName": "CHI",
                        "fullName": "Chicago Bulls",
                        "nickName": "Bulls",
                        "logo": "https://upload.wikimedia.org/wikipedia/fr/thumb/d/d1/Bulls_de_Chicago_logo.svg/1200px-Bulls_de_Chicago_logo.svg.png",
                        "score": {
                            "points": "107"
                        }
                    }
                },
                {
                    "seasonYear": "2021",
                    "league": "standard",
                    "gameId": "9649",
                    "startTimeUTC": "2021-10-31T00:00:00.000Z",
                    "endTimeUTC": "2021-10-31T02:20:00.000Z",
                    "arena": "FedExForum",
                    "city": "Memphis",
                    "country": "USA",
                    "clock": "",
                    "gameDuration": "2:10",
                    "currentPeriod": "4/4",
                    "halftime": "0",
                    "EndOfPeriod": "0",
                    "seasonStage": "2",
                    "statusShortGame": "3",
                    "statusGame": "Finished",
                    "vTeam": {
                        "teamId": "20",
                        "shortName": "MIA",
                        "fullName": "Miami Heat",
                        "nickName": "Heat",
                        "logo": "https://upload.wikimedia.org/wikipedia/fr/thumb/1/1c/Miami_Heat_-_Logo.svg/1200px-Miami_Heat_-_Logo.svg.png",
                        "score": {
                            "points": "129"
                        }
                    },
                    "hTeam": {
                        "teamId": "19",
                        "shortName": "MEM",
                        "fullName": "Memphis Grizzlies",
                        "nickName": "Grizzlies",
                        "logo": "https://upload.wikimedia.org/wikipedia/en/thumb/f/f1/Memphis_Grizzlies.svg/1200px-Memphis_Grizzlies.svg.png",
                        "score": {
                            "points": "103"
                        }
                    }
                },
                {
                    "seasonYear": "2021",
                    "league": "standard",
                    "gameId": "9650",
                    "startTimeUTC": "2021-10-31T00:00:00.000Z",
                    "endTimeUTC": "2021-10-31T02:24:00.000Z",
                    "arena": "Fiserv Forum",
                    "city": "Milwaukee",
                    "country": "USA",
                    "clock": "",
                    "gameDuration": "2:11",
                    "currentPeriod": "4/4",
                    "halftime": "0",
                    "EndOfPeriod": "0",
                    "seasonStage": "2",
                    "statusShortGame": "3",
                    "statusGame": "Finished",
                    "vTeam": {
                        "teamId": "31",
                        "shortName": "SAS",
                        "fullName": "San Antonio Spurs",
                        "nickName": "Spurs",
                        "logo": "https://upload.wikimedia.org/wikipedia/fr/0/0e/San_Antonio_Spurs_2018.png",
                        "score": {
                            "points": "102"
                        }
                    },
                    "hTeam": {
                        "teamId": "21",
                        "shortName": "MIL",
                        "fullName": "Milwaukee Bucks",
                        "nickName": "Bucks",
                        "logo": "https://upload.wikimedia.org/wikipedia/fr/3/34/Bucks2015.png",
                        "score": {
                            "points": "93"
                        }
                    }
                },
                {
                    "seasonYear": "2021",
                    "league": "standard",
                    "gameId": "9651",
                    "startTimeUTC": "2021-10-31T00:30:00.000Z",
                    "endTimeUTC": "2021-10-31T02:42:00.000Z",
                    "arena": "Chase Center",
                    "city": "San Francisco",
                    "country": "USA",
                    "clock": "",
                    "gameDuration": "2:02",
                    "currentPeriod": "4/4",
                    "halftime": "0",
                    "EndOfPeriod": "0",
                    "seasonStage": "2",
                    "statusShortGame": "3",
                    "statusGame": "Finished",
                    "vTeam": {
                        "teamId": "25",
                        "shortName": "OKC",
                        "fullName": "Oklahoma City Thunder",
                        "nickName": "Thunder",
                        "logo": "https://upload.wikimedia.org/wikipedia/fr/thumb/4/4f/Thunder_d%27Oklahoma_City_logo.svg/1200px-Thunder_d%27Oklahoma_City_logo.svg.png",
                        "score": {
                            "points": "82"
                        }
                    },
                    "hTeam": {
                        "teamId": "11",
                        "shortName": "GSW",
                        "fullName": "Golden State Warriors",
                        "nickName": "Warriors",
                        "logo": "https://upload.wikimedia.org/wikipedia/fr/thumb/d/de/Warriors_de_Golden_State_logo.svg/1200px-Warriors_de_Golden_State_logo.svg.png",
                        "score": {
                            "points": "103"
                        }
                    }
                },
                {
                    "seasonYear": "2021",
                    "league": "standard",
                    "gameId": "9652",
                    "startTimeUTC": "2021-10-31T01:00:00.000Z",
                    "endTimeUTC": "",
                    "arena": "Target Center",
                    "city": "Minneapolis",
                    "country": "USA",
                    "clock": "3:31",
                    "gameDuration": "1:57",
                    "currentPeriod": "4/4",
                    "halftime": "0",
                    "EndOfPeriod": "0",
                    "seasonStage": "2",
                    "statusShortGame": "2",
                    "statusGame": "In Play",
                    "vTeam": {
                        "teamId": "9",
                        "shortName": "DEN",
                        "fullName": "Denver Nuggets",
                        "nickName": "Nuggets",
                        "logo": "https://upload.wikimedia.org/wikipedia/fr/thumb/3/35/Nuggets_de_Denver_2018.png/180px-Nuggets_de_Denver_2018.png",
                        "score": {
                            "points": "89"
                        }
                    },
                    "hTeam": {
                        "teamId": "22",
                        "shortName": "MIN",
                        "fullName": "Minnesota Timberwolves",
                        "nickName": "Timberwolves",
                        "logo": "https://upload.wikimedia.org/wikipedia/fr/thumb/d/d9/Timberwolves_du_Minnesota_logo_2017.png/200px-Timberwolves_du_Minnesota_logo_2017.png",
                        "score": {
                            "points": "89"
                        }
                    }
                },
                {
                    "seasonYear": "2021",
                    "league": "standard",
                    "gameId": "9653",
                    "startTimeUTC": "2021-10-31T02:00:00.000Z",
                    "endTimeUTC": "",
                    "arena": "Footprint Center",
                    "city": "Phoenix",
                    "country": "USA",
                    "clock": "",
                    "gameDuration": "0:52",
                    "currentPeriod": "2/4",
                    "halftime": "1",
                    "EndOfPeriod": "1",
                    "seasonStage": "2",
                    "statusShortGame": "2",
                    "statusGame": "In Play",
                    "vTeam": {
                        "teamId": "7",
                        "shortName": "CLE",
                        "fullName": "Cleveland Cavaliers",
                        "nickName": "Cavaliers",
                        "logo": "https://upload.wikimedia.org/wikipedia/fr/thumb/0/06/Cavs_de_Cleveland_logo_2017.png/150px-Cavs_de_Cleveland_logo_2017.png",
                        "score": {
                            "points": "46"
                        }
                    },
                    "hTeam": {
                        "teamId": "28",
                        "shortName": "PHX",
                        "fullName": "Phoenix Suns",
                        "nickName": "Suns",
                        "logo": "https://upload.wikimedia.org/wikipedia/fr/5/56/Phoenix_Suns_2013.png",
                        "score": {
                            "points": "50"
                        }
                    }
                },
                {
                    "seasonYear": "2021",
                    "league": "standard",
                    "gameId": "9654",
                    "startTimeUTC": "2021-10-31T19:30:00.000Z",
                    "endTimeUTC": "",
                    "arena": "",
                    "city": "",
                    "country": "",
                    "clock": "",
                    "gameDuration": "",
                    "currentPeriod": "0/4",
                    "halftime": "",
                    "EndOfPeriod": "",
                    "seasonStage": "2",
                    "statusShortGame": "1",
                    "statusGame": "Scheduled",
                    "vTeam": {
                        "teamId": "30",
                        "shortName": "SAC",
                        "fullName": "Sacramento Kings",
                        "nickName": "Kings",
                        "logo": "https://upload.wikimedia.org/wikipedia/fr/thumb/9/95/Kings_de_Sacramento_logo.svg/1200px-Kings_de_Sacramento_logo.svg.png",
                        "score": {
                            "points": ""
                        }
                    },
                    "hTeam": {
                        "teamId": "8",
                        "shortName": "DAL",
                        "fullName": "Dallas Mavericks",
                        "nickName": "Mavericks",
                        "logo": "https://upload.wikimedia.org/wikipedia/fr/thumb/b/b8/Mavericks_de_Dallas_logo.svg/150px-Mavericks_de_Dallas_logo.svg.png",
                        "score": {
                            "points": ""
                        }
                    }
                },
                {
                    "seasonYear": "2021",
                    "league": "standard",
                    "gameId": "9655",
                    "startTimeUTC": "2021-10-31T23:00:00.000Z",
                    "endTimeUTC": "",
                    "arena": "",
                    "city": "",
                    "country": "",
                    "clock": "",
                    "gameDuration": "",
                    "currentPeriod": "0/4",
                    "halftime": "",
                    "EndOfPeriod": "",
                    "seasonStage": "2",
                    "statusShortGame": "1",
                    "statusGame": "Scheduled",
                    "vTeam": {
                        "teamId": "29",
                        "shortName": "POR",
                        "fullName": "Portland Trail Blazers",
                        "nickName": "Trail Blazers",
                        "logo": "https://upload.wikimedia.org/wikipedia/en/thumb/2/21/Portland_Trail_Blazers_logo.svg/1200px-Portland_Trail_Blazers_logo.svg.png",
                        "score": {
                            "points": ""
                        }
                    },
                    "hTeam": {
                        "teamId": "5",
                        "shortName": "CHA",
                        "fullName": "Charlotte Hornets",
                        "nickName": "Hornets",
                        "logo": "https://upload.wikimedia.org/wikipedia/fr/thumb/f/f3/Hornets_de_Charlotte_logo.svg/1200px-Hornets_de_Charlotte_logo.svg.png",
                        "score": {
                            "points": ""
                        }
                    }
                },
                {
                    "seasonYear": "2021",
                    "league": "standard",
                    "gameId": "9656",
                    "startTimeUTC": "2021-10-31T23:00:00.000Z",
                    "endTimeUTC": "",
                    "arena": "",
                    "city": "",
                    "country": "",
                    "clock": "",
                    "gameDuration": "",
                    "currentPeriod": "0/4",
                    "halftime": "",
                    "EndOfPeriod": "",
                    "seasonStage": "2",
                    "statusShortGame": "1",
                    "statusGame": "Scheduled",
                    "vTeam": {
                        "teamId": "40",
                        "shortName": "UTA",
                        "fullName": "Utah Jazz",
                        "nickName": "Jazz",
                        "logo": "https://upload.wikimedia.org/wikipedia/fr/3/3b/Jazz_de_l%27Utah_logo.png",
                        "score": {
                            "points": ""
                        }
                    },
                    "hTeam": {
                        "teamId": "21",
                        "shortName": "MIL",
                        "fullName": "Milwaukee Bucks",
                        "nickName": "Bucks",
                        "logo": "https://upload.wikimedia.org/wikipedia/fr/3/34/Bucks2015.png",
                        "score": {
                            "points": ""
                        }
                    }
                },
                {
                    "seasonYear": "2021",
                    "league": "standard",
                    "gameId": "9657",
                    "startTimeUTC": "2021-10-31T23:30:00.000Z",
                    "endTimeUTC": "",
                    "arena": "",
                    "city": "",
                    "country": "",
                    "clock": "",
                    "gameDuration": "",
                    "currentPeriod": "0/4",
                    "halftime": "",
                    "EndOfPeriod": "",
                    "seasonStage": "2",
                    "statusShortGame": "1",
                    "statusGame": "Scheduled",
                    "vTeam": {
                        "teamId": "10",
                        "shortName": "DET",
                        "fullName": "Detroit Pistons",
                        "nickName": "Pistons",
                        "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6a/Detroit_Pistons_primary_logo_2017.png/150px-Detroit_Pistons_primary_logo_2017.png",
                        "score": {
                            "points": ""
                        }
                    },
                    "hTeam": {
                        "teamId": "4",
                        "shortName": "BKN",
                        "fullName": "Brooklyn Nets",
                        "nickName": "Nets",
                        "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/44/Brooklyn_Nets_newlogo.svg/130px-Brooklyn_Nets_newlogo.svg.png",
                        "score": {
                            "points": ""
                        }
                    }
                }
            ]
        }
    }
    return res


def getMockGameDetail(gameId):
    res = {
        "api": {
            "status": 200,
            "message": "GET gameDetails/9650",
            "results": 1,
            "filters": [
                ""
            ],
            "game": [
                {
                    "seasonYear": "2021",
                    "league": "standard",
                    "gameId": "9650",
                    "startTimeUTC": "2021-10-31T00:00:00.000Z",
                    "endTimeUTC": "2021-10-31T02:24:00.000Z",
                    "arena": "Fiserv Forum",
                    "city": "Milwaukee",
                    "country": "USA",
                    "clock": "",
                    "gameDuration": "2:11",
                    "timesTied": "",
                    "leadChanges": "",
                    "currentPeriod": "4/4",
                    "halftime": "0",
                    "EndOfPeriod": "0",
                    "seasonStage": "2",
                    "statusShortGame": "3",
                    "statusGame": "Finished",
                    "vTeam": {
                        "fullName": "San Antonio Spurs",
                        "teamId": "31",
                        "nickname": "Spurs",
                        "logo": "https://upload.wikimedia.org/wikipedia/fr/0/0e/San_Antonio_Spurs_2018.png",
                        "shortName": "SAS",
                        "allStar": "0",
                        "nbaFranchise": "1",
                        "score": {
                            "win": "2",
                            "loss": "4",
                            "seriesWin": "1",
                            "seriesLoss": "1",
                            "linescore": [
                                "27",
                                "18",
                                "24",
                                "33"
                            ],
                            "points": "102"
                        },
                        "leaders": [
                            {
                                "points": "17",
                                "playerId": "897",
                                "name": "Derrick White"
                            },
                            {
                                "rebounds": "11",
                                "playerId": "1872",
                                "name": "Keldon Johnson"
                            },
                            {
                                "assists": "9",
                                "playerId": "382",
                                "name": "Dejounte Murray"
                            },
                            {
                                "points": "23",
                                "playerId": "382",
                                "name": "Dejounte Murray"
                            }
                        ]
                    },
                    "hTeam": {
                        "fullName": "Milwaukee Bucks",
                        "teamId": "21",
                        "nickname": "Bucks",
                        "logo": "https://upload.wikimedia.org/wikipedia/fr/3/34/Bucks2015.png",
                        "shortName": "MIL",
                        "allStar": "0",
                        "nbaFranchise": "1",
                        "score": {
                            "win": "3",
                            "loss": "3",
                            "seriesWin": "1",
                            "seriesLoss": "1",
                            "linescore": [
                                "24",
                                "23",
                                "20",
                                "26"
                            ],
                            "points": "93"
                        },
                        "leaders": [
                            {
                                "points": "28",
                                "playerId": "20",
                                "name": "Giannis Antetokounmpo"
                            },
                            {
                                "rebounds": "3",
                                "playerId": "115",
                                "name": "Pat Connaughton"
                            },
                            {
                                "assists": "1",
                                "playerId": "237",
                                "name": "George Hill"
                            },
                            {
                                "points": "16",
                                "playerId": "361",
                                "name": "Khris Middleton"
                            },
                            {
                                "assists": "3",
                                "playerId": "2207",
                                "name": "Justin Robinson"
                            },
                            {
                                "rebounds": "13",
                                "playerId": "20",
                                "name": "Giannis Antetokounmpo"
                            },
                            {
                                "rebounds": "8",
                                "playerId": "2408",
                                "name": "Thanasis Antetokounmpo"
                            },
                            {
                                "assists": "5",
                                "playerId": "361",
                                "name": "Khris Middleton"
                            }
                        ]
                    },
                    "officials": [
                        {
                            "name": "Matt Boland"
                        },
                        {
                            "name": "James Williams"
                        },
                        {
                            "name": "Evan Scott"
                        }
                    ]
                }
            ]
        }
    }
    return res

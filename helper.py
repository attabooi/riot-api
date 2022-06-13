import requests
import pandas as pd
from urllib import parse

class Helper:

  def setApi(self):
    global apiKey
    apiKey = myApi
    return apiKey, print(f'Your apiKey({apiKey}) is set.')

  def setId(self):
    global id
    id = nickname
    id = parse.quote(nickname)


    global puuid
    id = parse.quote(nickname)
    url = 'https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-name/' + id +'?api_key=' + apiKey
    r = requests.get(url)
    r = r.json()
    puuid = r['puuid']
    return id, puuid, print(f'Your puuid({puuid}) is set.(from {nickname})')

  # int for a number of matchId
  # find the latest games
  def getRankId(self,int):
    global rankId
    n = str(int)
    rankUrl = 'https://asia.api.riotgames.com/lol/match/v5/matches/by-puuid/' + puuid + '/ids?queue=420&type=ranked&start=0&count='+ n +'&api_key='+ apiKey
    r = requests.get(rankUrl)
    r = r.json()
    rankId = r
    return rankId, print(f'Your MatchId is set as "{rankId}".')

  def matchInfo(self, str):
    global info
    url = 'https://asia.api.riotgames.com/lol/match/v5/matches/' + str + '?api_key=' + apiKey
    r = requests.get(url)
    r = r.json()
    info = r['info']
    return info, print(f'Match information for {str}. It is set as "info".')

  def summonerName(self):
    summonerName = []
    for i in range(0,10):
      name = info['participants'][i]['summonerName']
      summonerName.append(name)
      gameId = info['gameId']
    return summonerName, print(f'Summoner names from a match(gameid : {gameId})')


nickname = '엉덩이요리사요한'
myApi = 'RGAPI-8f85ed0d-386f-47c6-b756-38f462529d49'


a = Helper()
a.setApi()
a.setId()
a.getRankId(5)
a.matchInfo('KR_5952405390')
a.summonerName()

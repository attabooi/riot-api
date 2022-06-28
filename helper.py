import requests
import pandas as pd
from urllib import parse

from ratelimit import limits, sleep_and_retry

ONE_MINUTE = 20
MAX_CALLS_PER_MINUTE = 30



@sleep_and_retry
@limits(calls=MAX_CALLS_PER_MINUTE, period=ONE_MINUTE)
class Helper:

  def __init__(self):
    pass
  
  # setting apiKey.
  def setApi(self, apikey):
    global apiKey
    apiKey = apikey
    print(f'Your apiKey({apiKey}) is set.')
    return apiKey

  # parsing nickname to get a puuid.
  def setId(self, nickname):
    global id
    id = parse.quote(nickname)

    global puuid
    id = parse.quote(nickname)
    url = 'https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-name/' + f'{id}' +'?api_key=' + f'{apiKey}'
    r = requests.get(url)
    r = r.json()
    print(r)
    puuid = r['puuid']
    print(f'Your puuid({puuid}) is set.(from {nickname})')
    return id, puuid

  # int for a number of matchId
  # find the latest games.
  def getRankId(self,int):
    global rankId
    n = str(int)
    rankUrl = 'https://asia.api.riotgames.com/lol/match/v5/matches/by-puuid/' + f'{puuid}' + '/ids?queue=420&type=ranked&start=0&count='+ f'{n}' +'&api_key='+ f'{apiKey}'
    r = requests.get(rankUrl)
    r = r.json()
    rankId = r
    print(f'Your MatchId is set as "{rankId}".')
    return rankId

  def matchInfo(self, str):
    global info
    url = 'https://asia.api.riotgames.com/lol/match/v5/matches/' + f'{str}' + '?api_key=' + f'{apiKey}'
    r = requests.get(url)
    r = r.json()
    info = r['info']
    print(f'Match information for {str}. It is set as "info".')
    return info

  # get 10 summonerNames in a game.
  def summonerName(self):
    summonerName = []
    for i in range(0,10):
      name = info['participants'][i]['summonerName']
      summonerName.append(name)
      gameId = info['gameId']
      print(f'Summoner names from a match(gameid : {gameId})')
    return summonerName

  # get summonerNames in a specific tier.
  def tierInfo(self, tier, division, page):
    url = 'https://kr.api.riotgames.com/lol/league-exp/v4/entries/RANKED_SOLO_5x5/' + f'{tier}' + '/' + f'{division}' + '?page='+ str(page) + '&api_key=' + f'{apiKey}'
    r = requests.get(url).json()
    num = len(r)
    print(f'got {num} of game data from {tier} {division}.')
    return r



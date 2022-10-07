from requests_html import HTMLSession
from bs4 import BeautifulSoup
from classes import Game

s = HTMLSession()

def formatDate(date):
    return date

def extract(date:str = ''):
    url = f'https://www.nba.com/games?date={date}' if date else 'https://www.nba.com/games'
    r = s.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    return soup

def transform(soup: BeautifulSoup):
    game_divs = soup.find_all('div', {'class': 'GameCard_gc__UCI46 GameCardsMapper_gamecard__pz1rg'})
    games = []
    for item in game_divs:
        game_type = item.find('span', {'class': 'GameCardMatchupStatusText_gcsPre__rnEtg'}).text
        team_names = [item.text for item in item.findAll('span', {'class': 'MatchupCardTeamName_teamName__9YaBA'})]
        is_live = bool(item.find('span', {'class': 'LiveBadge_lb__qV_my GameCardMatchupStatusText_gcsBadge__bWCRV'}))
        game_status = item.find('p', {'class':'GameCardMatchupStatusText_gcsText__PcQUX'}).text
        game_scores = [item.text for item in item.findAll('p', {'class': 'MatchupCardScore_p__dfNvc GameCardMatchup_matchupScoreCard__owb6w'})
        ] if is_live else None

        if game_status == 'Final': 
            game_scores = [item.text for item in item.findAll('p', {'class': 'MatchupCardScore_p__dfNvc GameCardMatchup_matchupScoreCard__owb6w'})]

        games.append(Game(game_type, team_names, is_live, game_status, game_scores))
    return games

soup = extract() # Extract content from webpage
games = transform(soup)

for game in games:
    print(game.type, game.teams, game.is_live, game.status, game.score)
# print(transform(soup)) # Get game divs

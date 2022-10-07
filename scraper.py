from requests_html import HTMLSession
from bs4 import BeautifulSoup

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
    for item in game_divs:
        game_type = item.find('span', {'class': 'GameCardMatchupStatusText_gcsPre__rnEtg'}).text
        team_names = item.findAll('span', {'class': 'MatchupCardTeamName_teamName__9YaBA'})
        team1, team2= team_names[0].text, team_names[1].text
        print(game_type)
        print(team1, team2)
    return

soup = extract() # Extract content from webpage
transform(soup)
# print(transform(soup)) # Get game divs

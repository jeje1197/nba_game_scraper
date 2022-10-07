import random
from requests_html import HTMLSession
from bs4 import BeautifulSoup

from datetime import datetime, timedelta
import pandas as pd

s = HTMLSession()

def extract(date:str = ''):
    url = f'https://www.nba.com/games?date={date}' if date else 'https://www.nba.com/games'
    r = s.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    return soup

def transform(soup: BeautifulSoup, date:str):
    game_divs = soup.find_all('div', {'class': 'GameCard_gc__UCI46 GameCardsMapper_gamecard__pz1rg'})
    games = []
    for item in game_divs:

        game_type_element = item.find('span', {'class': 'GameCardMatchupStatusText_gcsPre__rnEtg'})
        game_type = game_type_element.text if game_type_element else 'REGULAR SEASON'
        team_names = [item.text for item in item.findAll('span', {'class': 'MatchupCardTeamName_teamName__9YaBA'})]
        is_live = bool(item.find('span', {'class': 'LiveBadge_lb__qV_my GameCardMatchupStatusText_gcsBadge__bWCRV'}))
        game_status = item.find('p', {'class':'GameCardMatchupStatusText_gcsText__PcQUX'}).text
        game_scores = [item.text for item in item.findAll('p', {'class': 'MatchupCardScore_p__dfNvc GameCardMatchup_matchupScoreCard__owb6w'})
        ] if is_live else None

        # Team records eg. ["10-3","5-8"] -> [["10", "3"], ["5", "8"]]
        team_records = [item.text.split('-') for item in item.findAll('p', {'class': 'MatchupCardTeamRecord_record__20YHe'})]
        prediction = predict_winner(team_names, team_records)

        if game_status == 'Final': 
            game_scores = [item.text for item in item.findAll('p', {'class': 'MatchupCardScore_p__dfNvc GameCardMatchup_matchupScoreCard__owb6w'})]
            prediction = None

        game = {
            'Date': date,
            'Type': game_type,
            'Teams': team_names,
            'Live': is_live,
            'Prediction': prediction,
            'Status': game_status,
            'Score': f'{game_scores[0]}-{game_scores[1]}' if game_scores else None
        }
        games.append(game)
    return games


# Team names eg.["Kings", "Spurs"]
# Team records eg. [["10", "3"], ["5", "8"]]
def predict_winner(team_names:list[str], team_records:list[list[str]]):
    win_lose_ratios = []
    for list in team_records:
        num_wins = int(list[0])
        total_games_played = int(list[0]) + int(list[1])
        if total_games_played == 0:
            win_lose_ratios.append(0)
        else: 
            win_lose_ratios.append(num_wins/total_games_played)
    
    if win_lose_ratios[0] > win_lose_ratios[1]:
        return team_names[0]
    elif win_lose_ratios[0] > win_lose_ratios[1]:
        return team_names[1]
    else:
        return team_names[random.randint(0, 1)]


def make_predictions(num_days:int):
    all_games = []
    base_date = datetime.today()
    for i in range(num_days):
        cur_date = (base_date + timedelta(days=i)).strftime('%Y-%m-%d')
        soup = extract(cur_date) # Extract content from webpage
        games_for_day = transform(soup, cur_date)  # Create list of dictionaries from data
        all_games.extend(games_for_day)
    return all_games

def create_csv(games:list):
    df = pd.DataFrame(games) # Create dataframe
    print(df.head())

    current_time = datetime.now().strftime("%d-%m-%Y_%H-%M")
    df.to_csv(f'nbagames_{current_time}.csv') # Create csv file

games = make_predictions(30) # Make predictions for 30 days in advance
create_csv(games) # Store data in a csv file


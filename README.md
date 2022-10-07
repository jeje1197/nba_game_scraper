# NBA Web Scraper

This program makes predictions on which NBA teams will win their games in the next 30 days.

Tools Used: Python, BeautifulSoup, Pandas, MySQL

## How I created it
The core of this program can be broken into three parts:
1) Extraction
2) Transformation / Predictions
3) Storing

## Extraction
The extraction stage is where I collected data from '[https](https://www.nba.com/games)' using BeautifulSoup. BeautifulSoup
is a Python library for pulling data out of HTML and XML files.

## Transformation / Predictions
In the first half of this stage, all the information from the extraction stage was interpreted, formatted and grouped into
appropriate categories. Each of the main categories are as follows:
- team matchups
- team records
- game type (preseason, regular season, postseason)
- game status (start time / game clock),
- game score

At this point, the last thing that needed to be done was calculate predictions based on the data we observed. For the scope of this
project, I chose to give precedence mainly to team records. If a team had a better record than another team, they would be more likely
to win based on their play from the current season.

Once I finished writing the prediction algorithm, I stored the data for each game in a dictionary so each accessing each attribute would 
be simple and efficient. 

## Storing
Finally in order to make use of the data and compare the predictions to the actual results, I provided two ways to store it:
- in a CSV file
- in a MySQL database

I used Pandas to create a dataframe to convert to a .csv file and MySQL Connector to perform database operations.

## Future




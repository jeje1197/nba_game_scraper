# NBA Web Scraper

This program makes predictions on which NBA teams will win their games in the next 30 days.

Tools Used: Python, BeautifulSoup, Pandas

## How I created it
The core of this program can be broken into three parts:
1) Extraction
2) Transformation
3) Storing

## Extraction
The extraction stage is where I collected data from '[https](https://www.nba.com/games)' using BeautifulSoup. BeautifulSoup
is a Python library for pulling data out of HTML and XML files.

## Transformation
The transformation stage is where all the information from the extraction stages is interpreted, formatted and grouped into
its appropriate categories. The data I pulled from each game listing could be grouped into the following categories:
- team matchups
- game type (preseason, regular season, postseason)
- game status (start time / game clock),
- game score

In this stage, I took it a step further and added predictions to guess who would win the matchup for each game.

## Storing
Finally, once all the data for each game was properly formatted. I stored it in a .csv file using Pandas. This left the option for automating the prediction process to occur daily at specific intervals and storing the data in a database.



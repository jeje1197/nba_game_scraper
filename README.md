# NBA Web Scraper

This program fetches data about basketball games from the official NBA website and parses it into a CSV file.

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

## Storing
Finally, once all the data for each game was properly formatted. I stored it in a .csv file using Pandas.



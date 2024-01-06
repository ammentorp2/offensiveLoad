import requests
from bs4 import BeautifulSoup
from bs4 import Comment
import pandas as pd
import datetime


def getTableByTeamAndYear(team: str, year: str):
    currentYear = datetime.date.today().year
    if int(year) >= currentYear:
        print("Cannot parse a future or ongoing season. Sorry.") #TODO debug why a current year is acting up
        exit(1)
    CONST_RUSHING_AND_RECEIVING_INDEX = 1
    CONST_URL = 'https://www.pro-football-reference.com/teams/' + team + '/' + year + '.htm#rushing_and_receiving'
    response = requests.get(CONST_URL)

    soup = BeautifulSoup(response.content, 'html.parser')

    elements = soup.find_all(string=lambda text: isinstance(text, Comment))

    tables = []
    for element in elements:
        if 'table' in element:
            try:
                tables.append(pd.read_html(element)[0])
            except:
                continue
    try:
        rushingAndReceivingTable = tables[CONST_RUSHING_AND_RECEIVING_INDEX];
    except IndexError:
        rushingAndReceivingTable = []
    
    return rushingAndReceivingTable

import numpy
from player import Player
from tableScraper import *

def formatNumber(number: float) -> float:
    if numpy.isnan(number):
        return 0.0
    return number

def formatPosition(position: str) -> str:
    if position != position:
        return 'N/A'
    return position

def formatPlayerName(name: str) -> str:
    name = name.replace("*", "");
    name = name.replace("+", "");
    return name

def formatPercentage(num1: int, num2: int) -> float:
    return round(num1 / num2 * 100, 2);

def parsePlayerData(team: str, year: str):
    rushingAndReceivingTable = getTableByTeamAndYear(team, year);

    rowsToCalculate = (len(rushingAndReceivingTable) - 1);
    currentRow = 0
    players = []
    while currentRow < rowsToCalculate:
        playerName = formatPlayerName(rushingAndReceivingTable.loc[currentRow]['Unnamed: 1_level_0']['Player']);
        playerPosition = formatPosition(rushingAndReceivingTable.loc[currentRow]['Unnamed: 3_level_0']['Pos'])
        playerRushingAttempts = formatNumber(rushingAndReceivingTable.loc[currentRow]['Rushing']['Att'])
        playerRushingYards = formatNumber(rushingAndReceivingTable.loc[currentRow]['Rushing']['Yds'])

        playerReceivingTargets = formatNumber(rushingAndReceivingTable.loc[currentRow]['Receiving']['Tgt'])
        playerReceivingYards = formatNumber(rushingAndReceivingTable.loc[currentRow]['Receiving']['Yds'])
        player = Player(playerName, playerPosition , playerRushingAttempts, playerRushingYards, playerReceivingTargets, playerReceivingYards)
        players.append(player)
        currentRow += 1


    ## start of actual "analytics" bit of it
    if len(players) == 0:
        return [];

    teamTotal = [player for player in players if player.name == "Team Total"][0]

    for player in players:
        player.rushingVolume = formatPercentage(player.rushAttempts, teamTotal.rushAttempts);
        player.rushingProduction = formatPercentage(player.rushYards, teamTotal.rushYards);
        player.receivingVolume = formatPercentage(player.targets, teamTotal.targets);
        player.receivingProduction = formatPercentage(player.receivingYards, teamTotal.receivingYards);
        player.scrimmageVolume = formatPercentage(player.rushAttempts + player.targets , teamTotal.rushAttempts + teamTotal.targets);
        player.scrimmageProduction = formatPercentage(player.rushYards + player.receivingYards , teamTotal.rushYards + teamTotal.receivingYards);

    return players;


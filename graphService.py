import matplotlib.pyplot as plt 
from playerService import parsePlayerData
from player import Player

expectedProduction = [0, 50, 100] 
actualProduction = [0, 50, 100]

def visualizeProduction(team: str, year: str, graph: str):
    playerData: list[Player] = parsePlayerData(team, year);

    plt.plot(expectedProduction, actualProduction)

    xPoints = [];
    yPoints = [];

    for player in playerData:
        if graph == 'Rushing':
            xPoints.append(float(player.getRushingVolume()))
            yPoints.append(float(player.getRushingProduction()));
        elif graph == 'Receiving':
            xPoints.append(float(player.getReceivingVolume()))
            yPoints.append(float(player.getReceivingProduction()));
        elif graph == 'Scrimmage':
            xPoints.append(float(player.getScrimmageVolume()))
            yPoints.append(float(player.getScrimmageProduction()));
        plt.annotate(player.getName(), (xPoints[-1], yPoints[-1]));
     
    plt.scatter(xPoints, yPoints, color= "blue", marker= "*", s=30) 


    plt.xlabel(graph + ' Volume') 
    plt.ylabel(graph + ' Production') 
     
    plt.title(graph + ' Volume v Production for the ' + year + ' ' + team.upper()) 
    
    plt.show()
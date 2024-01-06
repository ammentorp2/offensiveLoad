from graphService import *

# TODO end user expirience
    # Base level is you pick a team, year, and either rushing/receiving/scrimmage
    # Eventually we cna do multi select for teams and years

CONST_VALID_GRAPHS = ['Rushing', 'Receiving', 'Scrimmage'];

team = 'clt'
year = '2004'
graph = 'Receiving'

visualizeProduction(team, year, graph);
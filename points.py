import json
import urllib.request

from utils import *
from settings import *

playoffPlayers = []

# GGBBLL export for assignment stats and point calculations
with urllib.request.urlopen(CURRENT_GGBBLL_EXPORT) as f:
    GGBBLL = json.loads(f.read().decode('utf-8-sig'))

# GBBL GGBBLL for team mapping to print out points     
with urllib.request.urlopen(CURRENT_GBBL_EXPORT) as f:
    GBBL = json.loads(f.read().decode('utf-8-sig'))

season = GGBBLL["gameAttributes"]["season"]

# Create dictionary of all GBBL teams for mapping
GBBLDict = dict()
for team in GBBL['teams']:
	GBBLTid = team['tid']
	GBBLDict[GBBLTid] = team['region'] + " " + team['name']

# Create list of all GGBBLL players in playoffs
for player in GGBBLL["players"]:
    for stat in player["stats"]:
        if playoff_check(stat, season):
            playoffPlayers.append(find_player(player))

# Loop through all players in watchlist to calc and print points
for player in GGBBLL["players"]:
    if player["watch"] == True: 
        CAP_CHECK = cap_check(player)
        if CAP_CHECK == False:
            for stat in player["stats"]:
                if stat["playoffs"] == False and stat["season"] == season:
                    points = assign_points(stat, player, season)
                    if find_player(player) in playoffPlayers:
                        points += 4
                    print_points(points, player, GBBLDict)
        else:
            for stat in player["stats"]:
                if stat["playoffs"] == False and stat["season"] == season:
                    points = cap_points(stat, player, season)
                    if find_player(player) in playoffPlayers:
                        points += 7
                    print_cap_points(points, player, GBBLDict)
from assignments import GBBL
import json

from utils import *
from settings import CURRENT_GBBL_EXPORT, CURRENT_GGBBLL_EXPORT

playoffPlayers = []

# GGBBLL export for assignment stats and point calculations
GGBBLL = fetch_export(CURRENT_GGBBLL_EXPORT)

# GBBL GGBBLL for team mapping to print out points
GBBL = fetch_export(CURRENT_GBBL_EXPORT)

season = GGBBLL["gameAttributes"]["season"]

# Create dictionary of all GBBL teams for mapping
GBBLDict = {}
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
    if player["watch"] is True:
        CAP_CHECK = cap_check(player)
        if CAP_CHECK is False:
            for stat in player["stats"]:
                if stat["playoffs"] is False and stat["season"] == season:
                    points = assign_points(stat, player, season)
                    if find_player(player) in playoffPlayers:
                        points += 4
                    print_points(points, player, GBBLDict)
        else:
            for stat in player["stats"]:
                if stat["playoffs"] is False and stat["season"] == season:
                    points = cap_points(stat, player, season)
                    if find_player(player) in playoffPlayers:
                        points += 7
                    print_cap_points(points, player, GBBLDict)

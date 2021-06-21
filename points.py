import json
import urllib.request

from utils import *
from settings import *

# GGBBLL export for assignment stats and point calculations
with urllib.request.urlopen(CURRENT_GGBBLL_EXPORT) as f:
    GGBBLL = json.loads(f.read().decode('utf-8-sig'))

# GBBL export for team mapping to print out points     
with urllib.request.urlopen(CURRENT_GBBL_EXPORT) as f:
    GBBL = json.loads(f.read().decode('utf-8-sig'))

season = GGBBLL["gameAttributes"]["season"]

# Create dictionary of all GBBL teams for mapping
teamDict = dict()
for team in GBBL['teams']:
	teamTid = team['tid']
	teamDict[teamTid] = team['region'] + " " + team['name']

# Loop through all players in watchlist to calc and print points
for player in GGBBLL["players"]:
    if player["watch"] == True:
        points = 0
        CAP_CHECK = cap_check(player)
        if CAP_CHECK == False:
            for stat in player["stats"]:
                if stat["playoffs"] == False and stat["season"] == season:
                    points = assign_points(stat, player, season)
                    print_points(points, player, teamDict)
        else:
            for stat in player["stats"]:
                if stat["playoffs"] == False and stat["season"] == season:
                    points = cap_points(stat, player, season)
                    print_cap_points(points, player, teamDict)
import json
import urllib.request

from utils import *
from settings import *

with urllib.request.urlopen(CURRENT_GGBBLL_EXPORT) as f:
    export = json.loads(f.read().decode('utf-8-sig'))
        
with urllib.request.urlopen(CURRENT_GBBL_EXPORT) as f:
    gbbl_export = json.loads(f.read().decode('utf-8-sig'))

season = export["gameAttributes"]["season"]

teamDict = dict()
for team in gbbl_export['teams']:
	teamTid = team['tid']
	teamDict[teamTid] = team['region'] + " " + team['name']

for player in export["players"]:
    if player["watch"] == True: 
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
                    print_points(points, player, teamDict)
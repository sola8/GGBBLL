import json
import urllib.request

from utils import *
from settings import *

allPlayers = []

with urllib.request.urlopen(CURRENT_GBBL_EXPORT) as f:
    export = json.loads(f.read().decode('utf-8-sig'))

with open(CURRENT_LOCAL_GGBBLL_EXPORT, encoding='utf-8-sig') as f:
   ggbbll_export = json.load(f)

# Grab all current players from GBBL export
for player in export['players']:
    if (player['tid'] != -3 and player['tid'] != -2):
        allPlayers.append(player)

# Get the current GBBL season
currentYear = export["gameAttributes"]["season"]

with open(ASSIGNMENT_FILE_NAME, "r") as file:
    # Loop through .txt file with assignments in it
    for line in file:
        # Compare names in .txt file with names in export 
        # If match, take the player's info in export
        player = list(filter(lambda player: (find_player(player)) == line.strip(), allPlayers))[0]
        # Clear unneeded keys from player
        for key in list(player.keys()):
            if key not in player_keys: 
                del player[key]
        for rating in range(len(player["ratings"])):
            if player["ratings"][rating] != currentYear:
                del player["ratings"][rating]
                break
        # Convert GBBL tid to GGBBLL tid
        # Then, put them on the watch list
        player['tid'] = main_to_g_league(player)
        player['watch'] = True
        ggbbll_export['players'].append(player) # Append to list of total assignments

assignFile = CURRENT_LOCAL_GGBBLL_EXPORT.replace(".json", "_updated.json")

# Dump to assignments.json file to paste into GGBBLL export later
# Still need to figure out how to put assignments into GGBBLL export without C/P
# And this doesn't handle players with no last name...
with open(assignFile, "w") as o:
    print('Creating export...')
    json.dump(ggbbll_export, o)
    print('Export done.')
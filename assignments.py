import json

from utils import *
from settings import CURRENT_GBBL_EXPORT, CURRENT_LOCAL_GGBBLL_EXPORT, ASSIGNMENT_FILE_NAME

allPlayers = []

GBBL = fetch_export(CURRENT_GBBL_EXPORT)

with open(CURRENT_LOCAL_GGBBLL_EXPORT, encoding='utf-8-sig') as f:
    GGBBLL = json.load(f)

# Grab all rostered players from GBBL export
for player in GBBL['players']:
    if (player['tid'] >= 0):
        allPlayers.append(player)

# Get the current GBBL season
currentYear = GBBL["gameAttributes"]["season"]

with open(ASSIGNMENT_FILE_NAME, "r") as file:
    # Loop through .txt file with assignments in it
    for line in file:
        # Compare names in .txt file with names in export
        # If match, take the player's info
        player = list(filter(lambda player: 
                            (find_player(player)) == line.strip(), allPlayers))[0]
        # Clear unneeded keys
        for key in list(player.keys()):
            if key not in player_keys:
                del player[key]
        for rating in enumerate(player["ratings"]):
            if rating[1]['season'] != currentYear:
                del rating
                break
        # Convert GBBL tid to GGBBLL tid
        # Then, put them on the watch list
        player['tid'] = main_to_g_league(player)
        player['watch'] = True
        # Append to list of players in GGBBLL export
        GGBBLL['players'].append(player)

assignFile = CURRENT_LOCAL_GGBBLL_EXPORT.replace(".json", "_assigned.json")

# Dump to new file with assignments
with open(assignFile, "w") as o:
    print('Creating export...')
    json.dump(GGBBLL, o)
    print('Export done.')

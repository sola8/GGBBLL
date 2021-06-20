import math

## Constants & Maps

# Keys to keep for assignment transfer
player_keys = ['firstName', 
               'lastName', 
               'born', 
               'college', 
               'face', 
               'imgURL', 
               'tid', 
               'ratings', 
               'hgt', 
               'weight', 
               'pos']

# Names for all T1 CAPs
CAP_NAMES = ['Daniel Week-Drake', 'Wojciej Tomasz Szczesny', 'Rodney Okafor']

# GBBL -> GGBBLL tid mapping 
assignment_map = {
    '0': 31,
    '1': 12,
    '2': 11,
    '3': 8,
    '4': 25,
    '5': 2,
    '6': 23,
    '7': 30,
    '8': 7, 
    '9': 19,
    '10': 17,
    '11': 6,
    '12': 0,
    '13': 21,
    '14': 13,
    '15': 20,
    '16': 26,
    '17': 9,
    '18': 5,
    '19': 24,
    '20': 15,
    '21': 10,
    '22': 4,
    '23': 14,
    '24': 29,
    '25': 22,
    '26': 1,
    '27': 16,
    '28': 18,
    '29': 3,
    '30': 27,
    '31': 28
}

# GGBBLL -> GBBL tid mapping
points_map = {v:k for (k, v) in assignment_map.items()}

## Functions
def main_to_g_league(player):
    return assignment_map[str(player['tid'])]

def g_league_to_main(player):
    return int(points_map[player['tid']])

def cap_check(player):
    if(player['firstName'].strip() + " " + player['lastName'].strip()) in CAP_NAMES:
        return True
    else:
        return False

def print_points(points, player, teamDict):
    output = f"{player['firstName'].strip()} {player['lastName'].strip()} (@{teamDict[g_league_to_main(player)]}): {points} TP"
    print(output)

def print_cap_points(points, player, teamDict):
    output = f"{player['firstName'].strip()} {player['lastName'].strip()} (CAP) (@{teamDict[g_league_to_main(player)]}): {points} TP"
    print(output)

def find_player(player):
    if len(player['lastName']) == None:
        return player['firstName'].strip()
    elif len(player['firstName']) == None:
        return player['lastName'].strip()
    else:
        return player['firstName'].strip() + player['lastName'].strip()

def awardCount(player, season):
    awardCount = 0
    for award in player['awards']:
       if award["season"] == season:
            awardCount += 1
    return awardCount

def assign_points(stat, player, season):
    awards = awardCount(player, season)
    points = (math.ceil((0.01*stat['pts'])) + math.ceil((0.025*(stat['drb']+stat['orb']))) + math.ceil((0.12*stat['blk'])) + 
    math.ceil((0.15*stat['stl'])) + math.ceil((0.035*stat['ast'])) + (4 * awards))
    base = math.ceil((0.4*stat['gp'])+(0.2*stat['gs']))
    if (points < base):
        points = base
    return points

def cap_points(stat, player, season):
    pointMin = 30
    awards = awardCount(player, season)
    points = (math.ceil((0.015*stat['pts'])) + math.ceil((0.09*(stat['drb']+stat['orb']))) + math.ceil((0.3*stat['blk'])) + 
    math.ceil((0.25*stat['stl'])) + math.ceil((0.1*stat['ast'])) + (7 * awards))
    base = math.ceil((0.5*stat['gp'])+(0.5*stat['gs']))
    if (points < base) and (base >= 30):
        return base
    elif (points < base) and (base < 30):
        return pointMin
    else:
        return points
import urllib.request, json

assignment = []
i = 1
season = 2062
   
player_keys = ['firstName', 'lastName', 'born', 'college', 'face', 'imgURL', 
               'tid', 'ratings', 'hgt', 'weight', 'pos']

value = input("Input 1 to parse GBBL Export, 2 to parse GGBBLL export: ")

if (value == "1"):
    with urllib.request.urlopen('https://raw.githubusercontent.com/OptimalbeastGBBL/GBBL/main/GBBL_2062_Weeks1-2.json') as f:
        export = json.loads(f.read().decode('utf-8-sig'))
if value == "2":
    with open('/Users/sola/Documents/Ish/Sports Sim Ish/GGBL Exports/G-League/2061_GGBBLL_Preseason.json', encoding='utf-8-sig') as f:
        export = json.load(f)

if value == "1":     
    while True:
        fname = input("Enter first name of player: ")
        lname = input("Enter last name of player: ")
        if fname == "STOP" or lname == "STOP":
            break
        for player in export["players"]:
            if player["firstName"] == fname and lname == player["lastName"]:
                for key in list(player.keys()):
                    if key not in player_keys: 
                        del player[key]
                for rating in range(len(player["ratings"])):
                        if player["ratings"][rating] != season:
                            del player["ratings"][rating]
                            break
                if player["tid"] == 0:
                    player["tid"] = 31
                elif player["tid"] == 1:
                    player["tid"] = 12
                elif player["tid"] == 2:
                    player["tid"] = 11
                elif player["tid"] == 3:
                    player["tid"] = 8
                elif player["tid"] == 4:
                    player["tid"] = 25
                elif player["tid"] == 5:
                    player["tid"] = 2
                elif player["tid"] == 6:
                    player["tid"] = 23
                elif player["tid"] == 7:
                    player["tid"] = 30
                elif player["tid"] == 8:
                    player["tid"] = 7
                elif player["tid"] == 9:
                    player["tid"] = 19
                elif player["tid"] == 10:
                    player["tid"] = 17
                elif player["tid"] == 11:
                    player["tid"] = 6
                elif player["tid"] == 12:
                    player["tid"] = 0
                elif player["tid"] == 13:
                    player["tid"] = 21
                elif player["tid"] == 14:
                    player["tid"] = 13
                elif player["tid"] == 15:
                    player["tid"] = 20
                elif player["tid"] == 16:
                    player["tid"] = 26
                elif player["tid"] == 17:
                    player["tid"] = 9
                elif player["tid"] == 18:
                    player["tid"] = 5
                elif player["tid"] == 19:
                    player["tid"] = 24
                elif player["tid"] == 20:
                    player["tid"] = 15
                elif player["tid"] == 21:
                    player["tid"] = 10
                elif player["tid"] == 22:
                    player["tid"] = 4
                elif player["tid"] == 23:
                    player["tid"] = 14
                elif player["tid"] == 24:
                    player["tid"] = 29
                elif player["tid"] == 25:
                    player["tid"] = 22
                elif player["tid"] == 26:
                    player["tid"] = 1
                elif player["tid"] == 27:
                    player["tid"] = 16
                elif player["tid"] == 28:
                    player["tid"] = 18
                elif player["tid"] == 29:
                    player["tid"] = 3
                elif player["tid"] == 30:
                    player["tid"] = 27
                elif player["tid"] == 31:
                    player["tid"] = 28
                player["watch"] = True
                assignment.append(player)
    assign_data = json.dumps(assignment, indent=4) + ","
    with open('output.json', "w", encoding='utf-8-sig') as o:
       json.dump(assignment, o, indent=4)

if value == "2":
    for things in export:
        print(things)


   

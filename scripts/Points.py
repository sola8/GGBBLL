import json
import math

def calc(pts, trb, blk, stl, ast, count):
    awards = (4 * count)
    tp = (math.ceil((0.01*pts)) + math.ceil((0.025*trb)) + math.ceil((0.12*blk)) + 
    math.ceil((0.15*stl)) + math.ceil((0.035*ast)) + awards)
    base = math.ceil((0.4*gp)+(0.2*gs))
    if tp < base:
        tp = base
    return tp;

with open('2061_GGBBLL_Post_Playoffs.json', encoding='utf-8-sig') as f:
   export = json.load(f)
     
tin = input("Tid: ")
seas = 2061

points = []
fname = []
lname = []
i = count = j = 0
     
print("------------------------------------------------")
print('') 

for team in export['teams']: 
    if team["tid"] == int(tin):
        print("**@"+team["region"], team["name"],"Training Points:**")
        
        
for player in export['players']: # Create a function for this?
   if player["tid"] == int(tin) and player["watch"] == True:
     fname.append(player['firstName'])
     lname.append(player['lastName'])
     name = [i + " " + j for i,j in zip(fname,lname)]
     for stat in player["stats"]:
        if stat["playoffs"] == False and stat["season"] == seas:
             orb = (stat["orb"])
             drb = (stat["drb"])
             trb = (orb + drb)
             pts = (stat["pts"])
             stl = (stat["stl"])
             ast = (stat["ast"])
             blk = (stat["blk"])
             gp = (stat["gp"])
             gs = (stat["gs"])
        if stat["playoffs"] == True and stat["season"] == seas:
            count += 1
     for award in player["awards"]:
       if award["season"] == seas:
         count += 1
     for c in name:
         points.append(calc(pts, trb, blk, stl, ast, count))
     i += 1
     points = list(dict.fromkeys(points))
     orb = drb = trb = pts = stl = ast = blk = gp = gs = count = 0
  

    
while j in range(len(points)):
    print(fname[j], lname[j]+"'s", "TP:", points[j])
    j += 1
    
     
print('')      
print("------------------------------------------------")

import json
import math

def calc(pts, trb, blk, stl, ast, count, cap_chek):
    if cap_chek == "N":
        awards = (4 * count)
        tp = (math.ceil((0.015*pts)) + math.ceil((0.025*trb)) + math.ceil((0.12*blk)) + 
        math.ceil((0.15*stl)) + math.ceil((0.035*ast)) + awards)
        base = math.ceil((0.4*gp)+(0.2*gs))
    elif cap_chek == "Y":
        awards = (7 * count)
        tp = (math.ceil((0.015*pts)) + math.ceil((0.09*trb)) + math.ceil((0.3*blk)) + 
        math.ceil((0.25*stl)) + math.ceil((0.1*ast)) + awards)
        base = math.ceil((0.5*gp)+(0.5*gs))
    else:
        print("Not Y or N!")
        return ("N/A");
    if tp < base:
        tp = base
    return tp;

with open('2061_GGBBLL_Post_Playoffs.json', encoding='utf-8-sig') as f:
   data = json.load(f)

count = 0
orb = 0
drb = 0
trb = 0
pts = 0
stl = 0
ast = 0
blk = 0
gp = 0
gs = 0

pinput1 = input("First Name of Player: ")
pinput2 = input("Last Name of Player: ")
seas = input("Season: ")
cap_chek = input("CAP? (Y/N): ")

   
for each in data["players"]:
    if each["firstName"] == pinput1 and each["lastName"] == pinput2:
            for some in each["stats"]:
                if some["playoffs"] == False and some["season"] == int(seas):
                    orb += (some["orb"])
                    drb += (some["drb"])
                    trb += (orb + drb)
                    pts += (some["pts"])
                    stl += (some["stl"])
                    ast += (some["ast"])
                    blk += (some["blk"])
                    gp += (some["gp"])
                    gs += (some["gs"])
                if some["playoffs"] == True and some["season"] == int(seas):
                    count += 1
            for each in each["awards"]:
                if each["season"] == int(seas):
                  count += 1
               
    
tp = calc(pts, trb, blk, stl, ast, count, cap_chek)

print("------------------------------------------------")
print('') 
                     
print(pinput1,pinput2,"TP:", tp)

print('') 
print("------------------------------------------------")


        

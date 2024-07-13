from store_references import CITY_DICT, STORE_DICT,STATE_DICT
import json
from store_references import FEL_NAME, REP_NAME, AREA
from dataset_collection import geoloc, ASM_NAME, CSM_NAME, FEL_NAME, REP_NAME, FEL_AREA, AREA

COUNTRY_DATA_LIST = geoloc.get("Country")
REGION_DATA_LIST = geoloc.get("Region")
TERR_DATA_LIST = geoloc.get("Territory")
STORE_STATE_LIST = geoloc.get("store_state")
STORE_CITY_DATA = geoloc.get("store_city")
STORE_NAME_DATA = geoloc.get("store_name")


TSM_NAME = [
        "alvarez, joshua",
        "ballard, michael",
        "berner, norman",
        "boswell, boa",
        "broude, schuyler",
        "brown, chanel",
        "burks, javier",
        "bustos, dionnie",
        "caines, melanie",
        "camero, michael",
        "childers, josh",
        "dean, daniel",
        "defeo, marc",
        "deslate, jose",
        "douglas, leon",
        "drew, maurice",
        "edelen, joshua",
        "egeberg, stephanie",
        "forester, will",
        "fritsch, ricci",
        "giron, rafael",
        "gomez, jose",
        "gordon, marquis",
        "gutierres, david",
        "hardy, brian",
        "harris, abishai",
        "hart, keith",
        "hawkins, anthony",
        "herring, angelo",
        "huff, christopher",
        "hymovitz, amanda",
        "jacobe, john",
        "karoff, jason",
        "kay, jeremy",
        "keynejad, keivan",
        "khan, amina",
        "lallemand, walkens",
        "lalumiere, michelle",
        "leuthauser, lance",
        "logan, james",
        "ludwig, brenden",
        "marchio, benjamin",
        "marcum, michael",
        "marron, james",
        "marshall, autumn",
        "meinhardt, stephanie",
        "mitchell, howard",
        "montoya, cristian",
        "navarria, paul",
        "newby, byron",
        "ocasio, yancy",
        "paige, justin",
        "pearce, kyle",
        "peltier, anne",
        "perez, luis",
        "pilot, kelli",
        "pinson, ronald",
        "powell, cynthia",
        "rice, brandon",
        "romero, christian",
        "sami, asif",
        "sanjines, stevan",
        "schofield, john",
        "silva, josue",
        "smith, malcolm",
        "sorensen, jon",
        "sorrells, william",
        "spendlove, andrew",
        "stone, julet",
        "tally, donnell",
        "tarnecki, austin",
        "thames, juan",
        "tsai, cheng shyong",
        "urman, betsy",
        "warddrip, tyler",
        "warren, bryant",
        "wolf, leonard",
        "yanes, gabriel",
        "0",
        "grieco, carolyn",
        "hartigan, brian",
        "lacombe, seth",
        "lo curto, lisa",
        "oh, alex",
        "perrotti, richard",
        "white, david",
    ]

ASM_NAME_LIST = []
CSM_NAME_LIST = []
TSM_NAME_LIST = []
FEL_NAME_LIST = []
REP_NAME_LIST = []

REGION_LIST = []
AREA_LIST = []
FEL_AREA_LIST = []
STATE_LIST = []
TERR_LIST = []
CITY_LIST = []
STORE_LIST = []


for i in CSM_NAME.keys():
    if i.lower() not in CSM_NAME_LIST:
        CSM_NAME_LIST.append(i.lower())
for i in ASM_NAME.keys():
    if i.lower() not in ASM_NAME_LIST:
        ASM_NAME_LIST.append(i.lower()) 
for i in TSM_NAME:
    if i.lower() not in TSM_NAME_LIST:
        TSM_NAME_LIST.append(i.lower())  
for i in FEL_NAME.keys():
    if i.lower() not in FEL_NAME_LIST:
        FEL_NAME_LIST.append(i.lower())   
for i in REP_NAME.keys():
    if i.lower() not in REP_NAME_LIST:
        REP_NAME_LIST.append(i.lower()) 

for i in REGION_DATA_LIST:
    if i.lower() not in REGION_LIST:
        REGION_LIST.append(i.lower())   
for i in AREA.keys():
    if i.lower() not in AREA_LIST:
        AREA_LIST.append(i.lower())
for i in FEL_AREA.keys():
    if i.lower() not in FEL_AREA_LIST:
        FEL_AREA_LIST.append(i.lower())
for i in STATE_DICT.keys():
    if i.lower() not in STATE_LIST:
        STATE_LIST.append(i.lower())
for i in TERR_DATA_LIST:
    if i.lower() not in TERR_LIST:
        TERR_LIST.append(i.lower())
for i in CITY_DICT.keys():
    if i.lower() not in CITY_LIST:
        CITY_LIST.append(i.lower())
for i in STORE_NAME_DATA:
    if i.lower() not in STORE_LIST:
        STORE_LIST.append(i.lower())    


TSM_NAME_FINAL = []
ASM_NAME_FINAL = []
CSM_NAME_FINAL = []
FEL_NAME_FINAL = []
REP_NAME_FINAL = []

AREA_FINAL = []
TERRITORIES_FINAL = []

for i in AREA_LIST:
    text = str(i).lower()
    text = text.replace(", ", " ")
    AREA_FINAL.append(text)

for i in TSM_NAME_LIST:
    text = str(i).lower()
    text = text.replace(", ", " ")
    TSM_NAME_FINAL.append(text)

for i in ASM_NAME_LIST:
    text = str(i).lower()
    text = text.replace(", ", " ")
    ASM_NAME_FINAL.append(text)

for i in CSM_NAME_LIST:
    text = str(i).lower()
    text = text.replace(", ", " ")
    CSM_NAME_FINAL.append(text)

for i in FEL_NAME_LIST:
    text = str(i).lower()
    text = text.replace(", ", " ")
    FEL_NAME_FINAL.append(text)

for i in REP_NAME_LIST:
    text = str(i).lower()
    text = text.replace(", ", " ")
    REP_NAME_FINAL.append(text)

for i in TERR_LIST:
    text = str(i).lower()
    # text = text.replace(",", "")
    TERRITORIES_FINAL.append(text)
    
# print(Partner_LIST,Product_LIST,CITY_LIST,STATE_LIST,STORE_LIST,TERR_LIST,ASM_NAME,TSM_LIST)    

data = {
    "Region":REGION_LIST,
    "Area":AREA_FINAL,
    "ASM":ASM_NAME_FINAL,
    "CSM":CSM_NAME_FINAL,
    "TSM":TSM_NAME_FINAL,
    "FEL_NAME":FEL_NAME_FINAL,
    "REP_NAME":REP_NAME_FINAL,
    "Territories":TERRITORIES_FINAL,
    "State":STATE_LIST,
    "City":CITY_LIST,
    "STORE":STORE_LIST,
}

with open("files/data/dataset.json", "w") as f:
  json.dump(data, f, indent=4)
import random
import json
import torch
import sys 
sys.path.append("files")
from model import NeuralNet
from spacy_utils import bag_of_words, tokenize

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

with open('files/dealer/dealer_intents.json', 'r') as json_data:
    intents = json.load(json_data)

FILE = "files/dealer/dealer_model.pth"
data = torch.load(FILE)


input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data['all_words']
tags = data['tags']
model_state = data["model_state"]

model = NeuralNet(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)

def detect_dealer(input):
    input = str(input).lower()
    sentence = tokenize(input)
    X = bag_of_words(sentence, all_words)
    X = X.reshape(1, X.shape[0])
    X = torch.from_numpy(X).to(device)

    output = model(X)
    _, predicted = torch.max(output, dim=1)

    tag = tags[predicted.item()]

    probs = torch.softmax(output, dim=1)
    prob = probs[0][predicted.item()]
    if prob.item() > 0.90:
        for intent in intents['intents']:
            if tag == intent["tag"]:
                response = random.choice(intent['responses'])
                return response
    else:
        return " "


DEALERS = {
    "A&D WIRELESS": ["a&d wireless", "a&dwireless"],
    "ABM WIRELESS": ["abm wireless", "abmwireless"],
    "ACTIVE COMMUNICATIONS": ["activecommunications", "active communications"],
    "ADVANCED CELLULAR & WIRELESS": [
        "advancedcellular&wireless",
        "advanced cellular & wireless",
    ],
    "AIR TIME COMMUNICATIONS": ["airtimecommunications", "air time communications"],
    "AK & 5 PILLARS LLC": ["ak & 5 pillars llc", "ak&5pillarsllc"],
    "ANIKA WIRELESS, INC.": ["anika wireless, inc.", "anikawireless,inc."],
    "APEX CELLULAR": ["apexcellular", "apex cellular"],
    "APEX COMMUNICATIONS - ARKANSAS": [
        "apex communications arkansas",
        "apexcommunications arkansas",
    ],
    "AT WIRELESS INC": ["atwirelessinc", "at wireless inc"],
    "AUDIOCARVE": ["audiocarve"],
    "Alliance Mobile": ["alliancemobile", "alliance mobile"],
    "BLUE GRAPES COMM LLC": ["bluegrapescommllc", "blue grapes comm llc"],
    "BLUELINKWIRELESS,LLC": ["bluelinkwireless,llc"],
    "BM MOBILE LLC": ["bm mobile llc", "bmmobilellc"],
    "BRANCH PATTON": ["branchpatton", "branch patton"],
    "BUG TUSSEL WIRELESS, LLC": ["bugtusselwireless,llc", "bug tussel wireless, llc"],
    "CB WIRELESS": ["cbwireless", "cb wireless"],
    "CELL SHOP INC": ["cellshopinc", "cell shop inc"],
    "CELL TECH MOBILITY LLC": ["celltechmobilityllc", "cell tech mobility llc"],
    "CELLULAR CONCEPTS": ["cellular concepts", "cellularconcepts"],
    "CELLULAR EXPRESS OF INDIANA": [
        "cellularexpressofindiana",
        "cellular express of indiana",
    ],
    "CELLULAR WORLD - NCA": ["cellularworldnca", "cellular world  nca"],
    "CELLULAR WORLD MI": ["cellularworldmi", "cellular world mi"],
    "CELLULARWORLD-329": ["cellularworld329"],
    "CF WIRELESS LLC": ["cfwirelessllc", "cf wireless llc"],
    "COMMUNICATE WIRELESS - OKC": [
        "communicatewirelessokc",
        "communicate wireless  okc",
    ],
    "CWSINC": ["cwsinc"],
    "DALATI BROTHERS INC.": ["dalati brothers inc.", "dalatibrothersinc."],
    "DIVERSITY WIRELESS PARTNERS LLC": [
        "diversitywirelesspartnersllc",
        "diversity wireless partners llc",
    ],
    "E WIRELESS": ["e wireless", "ewireless"],
    "EASTHAMPTON WIRELESS": ["easthamptonwireless", "easthampton wireless"],
    "ER COMMUNICATIONS INC DBA WELLCOMM": [
        "ercommunicationsincdbawellcomm",
        "er communications inc dba wellcomm",
    ],
    "EZ WIRELESS - GA": ["ezwirelessga", "ez wireless  ga"],
    "FCW, INC": ["fcw,inc", "fcw, inc"],
    "FONEPAGE COMMUNICATIONS INC": [
        "fonepagecommunicationsinc",
        "fonepage communications inc",
    ],
    "FTR COMMUNICATIONS LLC": ["ftrcommunicationsllc", "ftr communications llc"],
    "GASTONTELECOMMUNICATIONS,LLC": ["gastontelecommunications,llc"],
    "GSM AMERICA INC": ["gsm america inc", "gsmamericainc"],
    "Get Wireless Now": ["getwirelessnow", "get wireless now"],
    "Great Lakes Mobile": ["greatlakesmobile", "great lakes mobile"],
    "HADDAD ELECTRONICS": ["haddad electronics", "haddadelectronics"],
    "HATTAR WIRELESS": ["hattarwireless", "hattar wireless"],
    "HIGH MESA COMMUNICATIONS": ["highmesacommunications", "high mesa communications"],
    "IAG WIRELESS, LLC": ["iagwireless,llc", "iag wireless, llc"],
    "ISLAND CELLULAR GROUP INC.": [
        "island cellular group inc.",
        "islandcellulargroupinc.",
    ],
    "KIGER VENTURES LLC": ["kigerventuresllc", "kiger ventures llc"],
    "KYORAE TELECOM": ["kyoraetelecom", "kyorae telecom"],
    "LETS GO WIRELESS": ["lets go wireless", "letsgowireless"],
    "LIONS WIRELESS LLC": ["lions wireless llc", "lionswirelessllc"],
    "MAD MOUNTAIN WIRELESS": ["madmountainwireless", "mad mountain wireless"],
    "MAM COMMUNICATIONS INC": ["mam communications inc", "mamcommunicationsinc"],
    "MASTER WIRELESS HOLDINGS LLC": [
        "master wireless holdings llc",
        "masterwirelessholdingsllc",
    ],
    "MAXIMIS ENTERPRISE INC": ["maximis enterprise inc", "maximisenterpriseinc"],
    "MID TEX": ["mid tex", "midtex"],
    "MILLENIUM WIRELESS TECHNOLOGY INC": [
        "millenium wireless technology inc",
        "milleniumwirelesstechnologyinc",
    ],
    "MMS GROUP, INC.": ["mmsgroup,inc.", "mms group, inc."],
    "MOBILE EDGE": ["mobileedge", "mobile edge"],
    "MOBILETEL": ["mobiletel"],
    "MOBILY,LLC": ["mobily,llc"],
    "MOUNTAIN COMM & ELECTRONICS": [
        "mountain comm & electronics",
        "mountaincomm&electronics",
    ],
    "MUNDUS COMPANY LLC": ["munduscompanyllc", "mundus company llc"],
    "MYWIRELESS": ["mywireless"],
    "Midwest Wireless Technology": [
        "midwestwirelesstechnology",
        "midwest wireless technology",
    ],
    "NOBLE WIRELESS GROUP, LLC": [
        "noble wireless group, llc",
        "noblewirelessgroup,llc",
    ],
    "ONE TEL GROUP": ["one tel group", "onetelgroup"],
    "OPTIMUM WIRELESS, LLC": ["optimum wireless, llc", "optimumwireless,llc"],
    "OSCAR ORTIZ": ["oscarortiz", "oscar ortiz"],
    "PANORAMA COMMUNICATIONS, LLC": [
        "panorama communications, llc",
        "panoramacommunications,llc",
    ],
    "PINNACLE MOBILE LLC": ["pinnaclemobilellc", "pinnacle mobile llc"],
    "PORTABLES": ["portables"],
    "PREMIER TECHNOLOGIES WNY, LLC": [
        "premiertechnologieswny,llc",
        "premier technologies wny, llc",
    ],
    "PRIME COMMUNICATIONS - 58": [
        "prime communications  58",
        "primecommunications58",
        "prime",
    ],
    "PROTEL": ["protel"],
    "RINGUSWIRELESSLLC": ["ringuswirelessllc"],
    "ROCKY MOUNTAIN WIRELESS": ["rockymountainwireless", "rocky mountain wireless"],
    "S&K MOBIL SOLUTIONS LLC": ["s&k mobil solutions llc", "s&kmobilsolutionsllc"],
    "SIMPLE MOBILE ASSOCIATES, LLC": [
        "simplemobileassociates,llc",
        "simple mobile associates, llc",
    ],
    "SOUTHEAST COMMUNICATIONS GROUP LLC": [
        "southeastcommunicationsgroupllc",
        "southeast communications group llc",
    ],
    "SPEARHEADMOBILITYINC": ["spearheadmobilityinc"],
    "SPRING BUSINESS SOLUTIONS": [
        "spring business solutions",
        "springbusinesssolutions",
    ],
    "TELECOM WIRELESS": ["telecomwireless", "telecom wireless"],
    "THE CELLULAR TOUCH": ["the cellular touch", "thecellulartouch"],
    "THE WIRELESS EXPERIENCE GROUP": [
        "thewirelessexperiencegroup",
        "the wireless experience group",
    ],
    "TOTAL SOLUTIONS CORPORATION": [
        "total solutions corporation",
        "totalsolutionscorporation",
    ],
    "TS MOBILITY INC.": ["tsmobilityinc.", "ts mobility inc."],
    "USAWIRELESS": ["usawireless"],
    "Usa Wireless": ["usawireless", "usa wireless"],
    "VICTORIA COMM": ["victoriacomm", "victoria comm"],
    "VITAL WIRELESS, LLC": ["vital wireless, llc", "vitalwireless,llc"],
    "VIVID STRATEGIES, INC.": ["vividstrategies,inc.", "vivid strategies, inc."],
    "WECAN WIRELESS INC": ["wecanwirelessinc", "wecan wireless inc"],
    "WEST REGION MOBILITY L.L.C.": [
        "westregionmobilityl.l.c.",
        "west region mobility l.l.c.",
    ],
    "WIRELESS MANAGEMENT LLC": ["wirelessmanagementllc", "wireless management llc"],
    "WIRELESS PLUS - GA": ["wirelessplusga", "wireless plus  ga"],
    "WIRELESS SOLUTIONS, LLC": ["wirelesssolutions,llc", "wireless solutions, llc"],
    "WIRELESS TOUCH INC": ["wirelesstouchinc", "wireless touch inc"],
    "WORLDWIDE COMMUNICATIONS, INC. DBA UNIQ MOBILE": [
        "worldwidecommunications,inc.dbauniqmobile",
        "worldwide communications, " "inc. dba uniq mobile",
    ],
    "XIHUATRADINGINC": ["xihuatradinginc"],
    "ZAIN ENTERPRISES, LLC": ["zain enterprises, llc", "zainenterprises,llc"],
}



for i in DEALERS.keys():

    text = f"Sales for p8 for {i.lower()}."
    text = text.replace(", "," ")
    print(f"{i} -> {detect_dealer(text)}")
while True:
    text = input("Enter a question: ")
    print(detect_dealer(text))
    print()
# print(f"{text1} -> {detect_dealer(text1)}")    
# print(f"{text2} -> {detect_dealer(text2)}")    
# print(f"{text3} -> {detect_dealer(text3)}")    
# print(f"{text4} -> {detect_dealer(text4)}")    
# print(f"{text5} -> {detect_dealer(text5)}")    
# print(f"{text6} -> {detect_dealer(text6)}")    
# print(f"{text7} -> {detect_dealer(text7)}")    
# print(f"{text8} -> {detect_dealer(text8)}")    
# print(f"{text9} -> {detect_dealer(text9)}")    

import spacy

nlp = spacy.load("en_core_web_sm")
# Add new entity labels

def get_spacy_params(text):

    words = text.split()
    updated_words = []
    for i in words:
        updated_words.append(i.capitalize())

    input  = " ".join(updated_words) 
    # print(input)

    LOCATION = []
    PERSON = []
    DATE = []
    ORG = []
    OTHERS = []
    DETECTIONS = []
    doc = nlp(input)

    tokens = []
    for token in doc:
        # print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_,
        #         token.shape_, token.is_alpha, token.is_stop)
    # print("--")
        if token.is_stop == False:
            tokens.append(str(token.text))
    # print(tokens)    
    for ent in doc.ents:
        # print(ent.text, ent.label_)
        
        if ent.label_ == "PERSON":
            if str(ent.text).lower() not in ["banner"]:
                PERSON.append(str(ent.text).lower())
        elif ent.label_ == "GPE" or ent.label_ == "City" or ent.label_ == "LOC" :
            if str(ent.text).lower() not in ["verizon"]:
                LOCATION.append(str(ent.text).lower())
        elif ent.label_ == "ORG":
            ORG.append(str(ent.text).lower())
        elif ent.label_ == "DATE":
            date = str(ent.text)
            doc2 = nlp(date)
            tokens2 = []
            for token in doc2:
                tokens2.append(str(token.text))
            ind = tokens2.index(str(tokens2[0]))
            if int(ind) != 0:
                prev = tokens[(int(ind) - 1)]
                if prev.lower() in ["from","till"]:
                    DATE.append(f"{prev.lower()} {date.lower()}")
                else:    
                    DATE.append(date.lower())
            else:    
                DATE.append(date.lower())    
        else:
            OTHERS.append(str(ent.text).lower())

        if str(ent.text).lower() not in DETECTIONS:
            DETECTIONS.append(str(ent.text).lower())    
    for i in tokens:
        if str(i).lower() in ["q1","q2","q3","q4"]:
           DATE.append(str(i).lower())

    for i in tokens:
        if i.lower() in ["cor","dlr","rtl"]:
            ind = tokens.index(i)
            try:
                if ind >1:
                    if str(tokens[ind - 1]).lower() in ["stores", "store"] or str(tokens[ind + 1]).lower() in ["stores", "store"] or str(tokens[ind - 2]).lower() in ["stores", "store"] or str(tokens[ind + 2]).lower() in ["stores", "store"]: 
                        OTHERS.append(i.lower())
            except:
                pass

    mappings = {}
    if len(PERSON)!= 0 :
        mappings.update({"PERSON":PERSON})
    if len(LOCATION)!= 0 :
        mappings.update({"LOCATION":LOCATION})    
    if len(DATE)!= 0 :
        mappings.update({"DATE":DATE})
    if len(ORG)!= 0 :
        mappings.update({"ORG":ORG})
    if len(OTHERS)!= 0 :
        mappings.update({"OTHERS":OTHERS})

    return mappings

test_text = "What is the sales for P8a for stores under cellular world -329 / (prime) banner in AT&T?"

# print(get_spacy_params(test_text))
geoloc = {
"ASM": [
        "abbatematteo joseph",
        "alcala diana",
        "allen marvin",
        "black dollrethea (dee)",
        "cromartie carolyn",
        "jackson jason",
        "levy benay",
        "linnan tara",
        "meger jason",
        "norris payton",
        "shaffer suzzane",
        "stuart richard",
        "taylor michael",
        "tupper joshua"
    ],
    "CSM": [
        "wes cardwell",
        "aaron beatrez",
        "david daurora",
        "chantal makahanaloa",
        "marc stevens",
        "tim kreeft",
        "paul braddy",
        "andrew helms",
        "josh taylor",
        "jeff langlois"
    ],
    "TSM": [
        "alvarez joshua",
        "ballard michael",
        "berner norman",
        "boswell boa",
        "broude schuyler",
        "brown chanel",
        "burks javier",
        "bustos dionnie",
        "caines melanie",
        "camero michael",
        "childers josh",
        "dean daniel",
        "defeo marc",
        "deslate jose",
        "douglas leon",
        "drew maurice",
        "edelen joshua",
        "egeberg stephanie",
        "forester will",
        "fritsch ricci",
        "giron rafael",
        "gomez jose",
        "gordon marquis",
        "gutierres david",
        "hardy brian",
        "harris abishai",
        "hart keith",
        "hawkins anthony",
        "herring angelo",
        "huff christopher",
        "hymovitz amanda",
        "jacobe john",
        "karoff jason",
        "kay jeremy",
        "keynejad keivan",
        "khan amina",
        "lallemand walkens",
        "lalumiere michelle",
        "leuthauser lance",
        "logan james",
        "ludwig brenden",
        "marchio benjamin",
        "marcum michael",
        "marron james",
        "marshall autumn",
        "meinhardt stephanie",
        "mitchell howard",
        "montoya cristian",
        "navarria paul",
        "newby byron",
        "ocasio yancy",
        "paige justin",
        "pearce kyle",
        "peltier anne",
        "perez luis",
        "pilot kelli",
        "pinson ronald",
        "powell cynthia",
        "rice brandon",
        "romero christian",
        "sami asif",
        "sanjines stevan",
        "schofield john",
        "silva josue",
        "smith malcolm",
        "sorensen jon",
        "sorrells william",
        "spendlove andrew",
        "stone julet",
        "tally donnell",
        "tarnecki austin",
        "thames juan",
        "tsai cheng shyong",
        "urman betsy",
        "warddrip tyler",
        "warren bryant",
        "wolf leonard",
        "yanes gabriel",
        "0",
        "grieco carolyn",
        "hartigan brian",
        "lacombe seth",
        "lo curto lisa",
        "oh alex",
        "perrotti richard",
        "white david"
    ],
    "FEL_NAME": [
        "kimbrell barbara",
        "levy-westerdyk dana",
        "winfrey amy"
    ],
    "REP_NAME": [
        "adams shanon",
        "alvarez joshua",
        "applegate cameron",
        "ballard michael",
        "barrios mark",
        "bassford kyle",
        "berner norman",
        "bonilla tyrone",
        "boswell boa",
        "boulet aiden",
        "broude sky",
        "brown chanel",
        "burks javier",
        "bustos dionnie",
        "buzeta ronell",
        "caines melanie",
        "camero michael",
        "cha jason",
        "chiappone dominic",
        "childers josh",
        "choy wai cay (james)",
        "clark mary-helen",
        "dean daniel",
        "deslate jose",
        "doell vanessa",
        "douglas leon",
        "drew maurice",
        "durrell shawn",
        "egeberg stephanie",
        "fakih ali",
        "ferriss jeramie",
        "finnegan jeremy",
        "flanders chris",
        "forester will",
        "fritsch ricci",
        "giron rafael",
        "gordon marquis",
        "gorman thomas",
        "gottschalk casie",
        "grieco carolyn",
        "gutierres david",
        "hardy brian",
        "harris abishai",
        "hartigan brian",
        "hawkins anthony",
        "herring angelo",
        "huff christopher",
        "jacobe john",
        "jean-baptiste stanley",
        "karoff jason",
        "kay jeremy",
        "keynejad keivan",
        "khan amina",
        "khan raheel",
        "lacombe seth",
        "ladha noorin",
        "lallemand walkens",
        "lalumiere michelle",
        "larose jeremie",
        "lawson james",
        "leuthauser lance",
        "logan james",
        "ludwig brenden",
        "marchio benjamin",
        "marcum michael",
        "marron james",
        "marshall autumn",
        "mclean sadie",
        "mcmillan robert",
        "meinhardt stephanie",
        "mitchell howard",
        "momany todd",
        "montoya cristian",
        "navarria paul",
        "newby byron",
        "nguyen tommy",
        "ocasio yancy",
        "oh alex",
        "paige justin",
        "pearce kyle",
        "pelletier wayne",
        "peltier anne",
        "perez luis",
        "perrotti richard",
        "pilot kelli",
        "pineda aileen",
        "pinson ronald",
        "powell cynthia",
        "proulx marc-andre",
        "rice brandon",
        "romero christian",
        "sanchez ana",
        "sanjines stevan",
        "schofield john",
        "senchak donald",
        "silaphet stephen",
        "silva josue",
        "simpson brad",
        "smith jaylen",
        "smith malcolm",
        "sorensen jon",
        "sorrells william",
        "spendlove andrew",
        "stephens brian",
        "stone julet",
        "tally donnell",
        "tarnecki austin",
        "thames juan",
        "thompson quanette",
        "topfer richard",
        "tsai cheng shyong",
        "urman betsy",
        "warddrip tyler",
        "white david",
        "wolf leonard",
        "wong louie (li)",
        "wong tennyson",
        "yanes gabriel",
        "zwicker lawrence (dean)"
    ]
}   

ASM = geoloc.get("ASM")
CSM = geoloc.get("CSM")
TSM = geoloc.get("TSM")
FEL_NAME = geoloc.get("FEL_NAME")
REP_NAME = geoloc.get("REP_NAME")

# for i in REP_NAME:
#     text = f"Sales by {i} ."
#     print(f"{text} --> {get_spacy_params(text)}")


while True:
    text = input("Enter a question: ")
    print(get_spacy_params(text))
    print()

"""


"""
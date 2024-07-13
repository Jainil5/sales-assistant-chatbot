import spacy
from files.data.store_references import CITY_DICT, TERRITORY
from files.data.dataset_collection import geoloc
nlp = spacy.load("en_core_web_sm")
# Add new entity labels



    # tokens = []
    # for token in doc:
    # #     print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_,
    # #             token.shape_, token.is_alpha, token.is_stop)
    # # print("--")
    #     tokens.append(str(token.text))
    # print(tokens)    

c_list = CITY_DICT.keys()
country = geoloc.get("Country")
state = geoloc.get("store_state")
c_list2 = geoloc.get("store_city")

cities = []
c2 = []
ents = []
for i in c_list:
    doc = nlp(str(i))
    for ent in doc.ents:
        # label = str(ent.label_)
        # if label not in ents:
        #     ents.append(label)
        if ent.label_ == "LOC" or ent.label_ == "GPE" or ent.label_ == "FAC":    
            cities.append(i)
        elif ent.label_ != "PERSON":
            label = str(ent.label_)
            if label not in ents:
                ents.append(label)
for i in [country,state,c_list2]:
    doc = nlp(str(i))
    for ent in doc.ents:
        # label = str(ent.label_)
        # if label not in ents:
        #     ents.append(label)
        if ent.label_ == "LOC" or ent.label_ == "GPE" or ent.label_ == "FAC":    
            c2.append(i)
        elif ent.label_ != "PERSON":
            label = str(ent.label_)
            if label not in ents:
                ents.append(label)
                # print(ent.text, ent.label_)
notfound = []
nf2 = []
for i in c_list:
    if i not in cities:
        notfound.append(i)
for i in [country,state,c_list2]:
    if i not in c2:
        nf2.append(i)
print(notfound,nf2)
print(ents)

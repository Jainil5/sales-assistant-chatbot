from spacy_func import get_spacy_params
from type.type_fetch import detect_intent
from partner.partner_fetch import detect_partner
from product.product_fetch import detect_product
from coverage.coverage_fetch import detect_coverage
from region.region_fetch import detect_region
from dealer.dealer_fetch import detect_dealer
from store.store_fetch import detect_store
from area.area_fetch import detect_area

import json

with open('files/data/dataset.json', 'r') as json_data:
    json_data = json.load(json_data)
dataset = dict(json_data)

ASM = list(dataset.get("ASM"))
TSM = list(dataset.get("TSM"))
FEL_NAME = list(dataset.get("FEL_NAME"))
REP_NAME = list(dataset.get("REP_NAME"))

# print(ASM,TSM)
# print(dataset.values())

def get_params(input):
    text = str(input).lower()
    final_dict = {}

    area = detect_area(text)
    intent = detect_intent(text)
    partner = detect_partner(text)
    product = detect_product(text)
    coverage = detect_coverage(text)
    region = detect_region(text)
    dealer = detect_dealer(text)
    store = detect_store(text)

    # print(final_dict)
    spacy_output = get_spacy_params(text.capitalize())
    print(spacy_output)
    tsm_list = []
    asm_list = []
    fel_list = []
    rep_list = []
    dealer_list = []
    other_list = []
    location_list = []
    date_list = []
    if len(spacy_output)!=0:
        for param,values in spacy_output.items():
            if len(values) != 0:
                if param == "PERSON" :
                    for val in values:
                        if val.lower() in TSM:
                                tsm_list.append(val)  
                        elif val.lower() in ASM:
                                asm_list.append(val)  
                        elif val.lower() in FEL_NAME:
                                fel_list.append(val)
                        elif val.lower() in REP_NAME:
                                rep_list.append(val)
                        else:
                             other_list.append(val)            
                elif param == "LOCATION":
                    location_list.append(val)
                elif param == "DATE":
                    date_list.append(val)
                elif param == "OTHERS":
                    for val in values:
                        if val.lower() in ["cor","dlr","rtl"]:
                            dealer_list.append(val.lower())
                        else:
                            other_list.append(val)           
    

    if len(intent.strip()) != 0:
        final_dict.update({"intent":intent})
    if len(partner.strip()) != 0:
        final_dict.update({"partner":partner})
    if len(product.strip()) != 0:
        final_dict.update({"product":product})
    if len(coverage.strip()) != 0:
        final_dict.update({"coverage":coverage})
    if len(region.strip()) != 0:
        final_dict.update({"region":region})
    if len(dealer.strip()) != 0:
        final_dict.update({"dealer":dealer})       
    if len(store.strip()) != 0:
        final_dict.update({"store":store})  
    if len(asm_list) != 0:
        final_dict.update({"ASM":asm_list})
    if len(tsm_list) != 0:
        final_dict.update({"TSM":tsm_list})
    if len(fel_list) != 0:
        final_dict.update({"FEL_NAME":fel_list})
    if len(rep_list) != 0:
        final_dict.update({"REP_NAME":rep_list})
    if len(dealer_list) != 0:
        final_dict.update({"dealer_list":dealer_list})
    if len(other_list) != 0:
        final_dict.update({"other_list":other_list})
    if len(location_list) != 0:
        final_dict.update({"location_list":location_list})
    

    return final_dict

print(get_params("Sales of COR stores for last month for pixel 8a in Southeast area and aberdeen for Navarria Paul , Jackson Jason and Winfrey Amy. "))


# chantal makahanaloa
# oh alex
# perrotti richard
# white david
# tally donnell
# stone julet
# sami asif
# pearce kyle
# lalumiere michelle
# lallemand walkens
# brown chanel
# topfer richard
# tally donnell
# stone julet
# proulx marc-andre
# pineda aileen
# pearce kyle
# momany todd
# mclean sadie
# lalumiere michelle
# lallemand walkens
# forester will
# brown chanel
# barrios mark

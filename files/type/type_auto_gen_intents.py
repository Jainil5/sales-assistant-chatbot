import json
import random

intent_dict = {
    "traffic_data": [
        "traffic",
        "visitors",
        "website visitors",
        "hits",
        "visits",
        "sot",
        "share of traffic",
        "visit",
    ],
    "promotions_data": [
        "promotions",
        "promotion",
        "offer",
        "discount",
        "trade in",
        "switched",
        "bogo",
        "switcher",
        "tradein",
        "trade-in",
        "average selling price",
        "asp",
        "selling price",
        "attach rates",
        "total cost of ownership",
        "total cosumer cost",
        "consumer cost",
        "best cost",
        "best offer",
        "effective offer",
        "offer",
        "best offer",
        "effective offer",
    ],
    "sales_data": [
        "sellout",
        "units",
        "volume",
        "sales",
        "target",
        "achievement",
        "ach",
        "covered",
        "stores",
        "run-rate",
        "sale",
    ],
    "gfa_data": [
        "category",
        "driver",
        "drivers",
        "inventory",
        "stock",
        "product availability",
        "rsa knowledge",
        "rsa advocacy",
        "staff product knowledge",
        "promo knowledge",
        "staff knowledge",
        "rsa",
        "opinion",
        "opinions",
        "demo devices",
        "demo connectivity",
        "product demos",
        "merchandise connectivity",
        "demo",
        "visibility",
        "visible",
        "miscellaneous",
        "misc",
        "competitive pricing",
        "competitiveness",
    ],
}

final_list = []
join_sentence = ["for pixel","of google"]
for type in ["traffic_data","promotions_data","sales_data","gfa_data"]:
    sentence_list = []
    value = intent_dict.get(type)
    for val in value:
        for add in join_sentence:
            text = f"{val} {add}"
            sentence_list.append(text)    
    if type == "sales_data":
        additional_sentences = ["pixel 8 by AT&T","Top 10 performing stores in last 4 weeks.",
        "Sales of Great Lakes by David Daurora.",
        "What are the sales for att by fel name",
        "P8a Sales for att this week",
        "p8a sales for covered regions in att this week",
        "What are the sales for att by region?",
        "What are p7 sales last week?"
        ]
        sentence_list.extend(additional_sentences)
    dict = {"tag":type,"patterns":sentence_list,"responses":[type.lower()]}
    final_list.append(dict) 

for type in ["sales_inventory_data"]:
    sentence_list = []
    value = intent_dict.get("sales_data")
    value2 = intent_dict.get("gfa_data")
    for val in value:
        for val2 in value2:
            text = f"{val.lower()} and {val2.lower()} {join_sentence[(random.randint(0,1))]} "
            sentence_list.append(text)    
    
    dict = {"tag":type,"patterns":sentence_list,"responses":[type.lower()]}
    final_list.append(dict) 
    
general_ques = [
        "Why is overall sales decreasing?",
        "Which regions had the lowest sales?",
        "What are the regions affecting sales growth for this week in us",
        "Why is sales of pixel 8 increasing?",
      ]
top_10 = ["Top 10 stores", "top 10 performing stores in Aberdeen", "top 10 performing cities for pixel 8", "top 10 stores with highest inventory"]
dict = {"tag":"General","patterns":general_ques,"responses":["general_data"]}
final_list.append(dict) 

final_data = {"intents":final_list}


with open("files/type/type_auto_intents.json", "w") as file:
    json.dump(final_data, file, indent=4)
    
import json


AREA = {
    "Central Canada": ["central canada", "centralcanada"],
    "Eastern Canada": ["easterncanada", "eastern canada"],
    "Florida": ["florida"],
    "Great Lakes": ["great lakes", "greatlakes"],
    "Mid Atlantic North": ["midatlanticnorth", "mid atlantic north"],
    "Mid Atlantic South": ["midatlanticsouth", "mid atlantic south"],
    "New York": ["newyork", "new york"],
    "North Central": ["north central", "northcentral"],
    "Ohio Valley": ["ohio valley", "ohiovalley"],
    "Pac Northwest": ["pacnorthwest", "pac northwest"],
    "Pac Southwest": ["pacsouthwest", "pac southwest"],
    "Rocky Mtn": ["rockymtn", "rocky mtn", "rocky mountain"],
    "Southeast": ["southeast area", "southeast"],
    "Texas": ["texas"],
    "Western Canada": ["western canada", "westerncanada"],
}



final_list = []
for area, values in AREA.items():
    sentence_list = []
    sentence_list.append(area.lower())
    for i in values:
      if i.lower() not in sentence_list:
        sentence_list.append(i.lower())
    sentence_list.append(f"{area.lower()} area")  
    sentence_list.append(f"area {area.lower()}")  
    value = {"tag":area.lower(),"patterns":sentence_list,"responses":[area.lower()]}
    
    final_list.append(value)  

# print(final_list)

output_dict = {"intents":final_list}

with open("files/area/area_intents.json", "w") as file:
    json.dump(output_dict, file, indent=2)

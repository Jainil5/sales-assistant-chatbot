import json

region_list = ["east",
        "west",
        "central",
        "northeast",
        "southeast",
        "atlantic north",
        "atlantic south",
        "coastal plains",
        "great lakes",
        "mountain",
        "pacific",
        "south"]

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

# Southeast

final_list = []
for region in region_list:
  sentence_list = []
  sentence_list.append(region.lower())
  sentence_list.append(f"{region.lower()} region")  
  sentence_list.append(f"region {region.lower()}")  
  value = {"tag":region.lower(),"patterns":sentence_list,"responses":[region.lower()]}
  
  final_list.append(value)  

# print(final_list)

output_dict = {"intents":final_list}

with open("files/region/region_auto_intents.json", "w") as file:
    json.dump(output_dict, file, indent=2)

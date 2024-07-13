import json

with open('files\data\dataset.json', 'r') as f:
    json_data = json.load(f)

dataset = dict(json_data)
ASM = list(dataset.get("ASM"))
CSM = list(dataset.get("CSM"))
TSM = list(dataset.get("TSM"))
FEL_NAME = list(dataset.get("FEL_NAME"))
REP_NAME = list(dataset.get("REP_NAME"))

print(ASM,CSM,TSM,FEL_NAME,REP_NAME)
# final_list = []
# for key, vals in person.items():
    
#   person_list = []
#   person_list.append(key.lower())
#   for i in vals:
#     if i.lower() not in person_list:
#         person_list.append(i.lower())
#     if "," in i:
#         filter = i.replace(",", "")
#         if filter.lower() not in person_list:    
#             person_list.append(filter)
#     if "-" in i:
#         filter = i.replace("-", "")
#         if filter.lower() not in person_list:
#             person_list.append(filter)


#   value = {"tag":key.lower(),"patterns":person_list,"responses":[key.lower()]}
  
#   final_list.append(value)  

# # print(final_list)

# output_dict = {"intents":final_list}

# with open("files/person/person_intents.json", "w") as file:
#     json.dump(output_dict, file, indent=2)


import random
import json
import torch
import sys 
sys.path.append("files")
from model import NeuralNet
from spacy_utils import bag_of_words, tokenize
# from nltk_utils import bag_of_words, tokenize

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

with open('files/region/region_intents.json', 'r') as json_data:
    intents = json.load(json_data)


FILE = "files/region/region_model.pth"
data = torch.load(FILE)


input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data['all_words']
tags = data['tags']
model_state = data["model_state"]

model = NeuralNet(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)

def detect_region(input):
    input = str(input).lower()
    sentence = tokenize(input)
    X = bag_of_words(sentence, all_words)
    X = X.reshape(1, X.shape[0])
    X = torch.from_numpy(X).to(device)

    output = model(X)
    print(output)
    _, predicted = torch.max(output, dim=1)

    tag = tags[predicted.item()]

    probs = torch.softmax(output, dim=1)
    prob = probs[0][predicted.item()]
    if prob.item() > 0.70:
        for intent in intents['intents']:
            if tag == intent["tag"]:
                response = random.choice(intent['responses'])
                return response
    else:
        return " "

while True:
    text = input("Enter a question: ")
    print(detect_region(text))
    print()



text1 = "top 10 covered stores in southeast"
text2 = "Sales of pixel 8 in florida by bby in stored that are in region"
text3 = "pixel 8 by AT&T in covered places"
text4 = "Sales of pixel 8 in places that are not covered"
text5 = "Sales of uncovered area?"
text6 = "Sales of pixel 7 by Verizon where region is uncovered?"
text7 = "Sales for p8pro by vzn for uncovered"

# print(detect_region(text1))    
# print(detect_region(text2))    
# print(detect_region(text3))    
# print(detect_region(text4))    
# print(detect_region(text5))   
# print(detect_region(text6)) 
# print(detect_region(text7))   

# region_list = ["east",
#         "west",
#         "central",
#         "northeast",
#         "southeast",
#         "atlantic north",
#         "atlantic south",
#         "coastal plains",
#         "great lakes",
#         "mountain",
#         "pacific",
#         "south"]

# for i in region_list:
#     text = f"Sales in {i}."
#     print(f"{text} -> {detect_region(text)}")
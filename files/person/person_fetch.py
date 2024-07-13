import random
import json
import torch
import sys 
sys.path.append("files")
from model import NeuralNet
from spacy_utils import bag_of_words, tokenize
# from nltk_utils import bag_of_words, tokenize

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

with open('files/partner/partner_intents.json', 'r') as json_data:
    intents = json.load(json_data)


FILE = "files/partner/partner_model.pth"
data = torch.load(FILE)


input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data['all_words']
tags = data['tags']
model_state = data["model_state"]

model = NeuralNet(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)

def detect_partner(input):
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
    if prob.item() > 0.50:
        for intent in intents['intents']:
            if tag == intent["tag"]:
                response = random.choice(intent['responses'])
                return response
    else:
        return ""




text1 = "top 10 stores perform in usa for last week in marysville "
text2 = "what is inventory of pixel 8 in florida by AT&T?"
text3 = "PROMOTIONS OF PIXEL 8 BY AT&T"
text4 = "Sales of pixel 7 by Verizon?"
text5 = "Sles of pixel 8 in florida by bby"
text6 = "pixel 8 by rogers"
text7 = "Sales for p8pro by vzn"
text8 = "Sales for p8pro by TELUS"
text9 = "Sales for p8pro by BELL"

# print(detect_partner(text1))    
# print(detect_partner(text2))    
# print(detect_partner(text3))    
# print(detect_partner(text4))    
# print(detect_partner(text5))   
# print(detect_partner(text6)) 
# print(detect_partner(text7))   
# print(detect_partner(text8))   
# print(detect_partner(text9))   

 

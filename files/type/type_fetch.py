import random
import json
import torch
import sys 
sys.path.append("files")
from model import NeuralNet
from spacy_utils import bag_of_words, tokenize
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

with open('files/type/type_intents.json', 'r') as json_data:
    intents = json.load(json_data)

FILE = "files/type/type_model.pth"
data = torch.load(FILE)

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data['all_words']
tags = data['tags']
model_state = data["model_state"]

type_model = NeuralNet(input_size, hidden_size, output_size).to(device)
type_model.load_state_dict(model_state)

def detect_intent(input):
    input = str(input).lower()
    sentence = tokenize(input)
    X = bag_of_words(sentence, all_words)
    X = X.reshape(1, X.shape[0])
    X = torch.from_numpy(X).to(device)

    output = type_model(X)
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
        return " "


text1 = "traffic for samsung"
text2 = "what is inventory of pixel 8 in florida?"
text3 = "Why is pixel 8 sales increasing?"

text4 = "Sales of pixel 7 by Verizon?"
text5 = "Sales of pixel 8 in florida"
text6 = "pixel 8 by AT&T"
text7 = "What is sales of west region for att for pixel 8a"

# print(detect_intent(text1))    
# print(detect_intent(text2))    
# print(detect_intent(text3))    
# print(detect_intent(text4))    
# print(detect_intent(text5))   
# print(detect_intent(text6)) 
# print(detect_intent(text7))   
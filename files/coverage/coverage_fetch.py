import random
import json
import torch
import sys 
sys.path.append("files")
from model import NeuralNet
from spacy_utils import bag_of_words, tokenize

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

with open('files/coverage/coverage_intents.json', 'r') as json_data:
    intents = json.load(json_data)


FILE = "files/coverage/coverage_model.pth"
data = torch.load(FILE)


input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data['all_words']
tags = data['tags']
model_state = data["model_state"]

model = NeuralNet(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)

def detect_coverage(input):
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
    if prob.item() > 0.75:
        for intent in intents['intents']:
            if tag == intent["tag"]:
                response = random.choice(intent['responses'])
                return response
    else:
        return " "




text1 = "top 10 stores"
text2 = "Sales of pixel 8 in florida by bby in stored that are in coverage"
text3 = "pixel 8 by AT&T in covered places"
text4 = "Sales of pixel 8 in places that are not covered"
text5 = "Sales of uncovered area?"
text6 = "Sales of pixel 7 by Verizon where coverage is uncovered?"
text7 = "Sales for p8pro by vzn for uncovered"

# print(detect_coverage(text1))    
# print(detect_coverage(text2))    
# print(detect_coverage(text3))    
# print(detect_coverage(text4))    
# print(detect_coverage(text5))   
# print(detect_coverage(text6)) 
# print(detect_coverage(text7))   

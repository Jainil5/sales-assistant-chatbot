import random
import json
import torch
import sys 
sys.path.append("files")
from model import NeuralNet
from spacy_utils import bag_of_words, tokenize

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

with open('files/product/product_intents.json', 'r') as json_data:
    intents = json.load(json_data)

FILE = "files/product/product_model.pth"
data = torch.load(FILE)


input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data['all_words']
tags = data['tags']
model_state = data["model_state"]

model = NeuralNet(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)

def detect_product(input):
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
    if prob.item() > 0.90:
        for intent in intents['intents']:
            if tag == intent["tag"]:
                response = random.choice(intent['responses'])
                return response
    else:
        return " "



text1 = "promotion of p8pro"
text2 = "sales of p8a in texas"
text3 = "pixel 8 pro in florida"
text4 = "Why is pixel 8a sale increasing?"
text5 = "what is inventory of PIXEL 8A in florida?"
text6 = "gogle p 7 by AT&T"
text7 = "p 8 by AT&T"
text8 = "Why is p8pro sale increasing?"
text9 = "WHY IS  pixel 8a SALE INCREASING?"
text10 = "Sales for covered doors for ATT"



# print(f"{text1} -> {detect_product(text1)}")    
# print(f"{text2} -> {detect_product(text2)}")    
# print(f"{text3} -> {detect_product(text3)}")    
# print(f"{text4} -> {detect_product(text4)}")    
# print(f"{text5} -> {detect_product(text5)}")    
# print(f"{text6} -> {detect_product(text6)}")    
# print(f"{text7} -> {detect_product(text7)}")    
# print(f"{text8} -> {detect_product(text8)}")    
# print(f"{text9} -> {detect_product(text9)}")    
# print(f"{text10} -> {detect_product(text10)}")    

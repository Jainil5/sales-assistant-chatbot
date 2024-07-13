import sys
sys.path.append("files")
from files.app import get_params



text1 = "Covered Run rate of pixel 8 by jackson jason and navarria paul for verizon in marysville"
text2 = "promotions of p8a for Q1 by bby in New York "
text3 = "p8pro from 2022 in USA"
text4 = "Why is pixel 8a sale increasing in Canada?"
text5 = "what is inventory of PIXEL 8A in florida for partner verizon ?"
text6 = "gogle p 7 by tmobile in Texas this month "
text7 = "p 8 by AT&T in las vegas from 2022"
text8 = "What is the sales for P8a for DLR stores under cellular world -329 / (prime) banner in AT&T?"
text9 = "WHY IS  PIXEL 6 SALE INCREASING BY ATT?"


print(f"{text1} -> {get_params(text1)}\n")    
print(f"{text2} -> {get_params(text2)}\n")    
print(f"{text3} -> {get_params(text3)}\n")    
print(f"{text4} -> {get_params(text4)}\n")    
print(f"{text5} -> {get_params(text5)}\n")    
print(f"{text6} -> {get_params(text6)}\n")    
print(f"{text7} -> {get_params(text7)}\n")    
print(f"{text8} -> {get_params(text8)}\n")    
print(f"{text9} -> {get_params(text9)}\n")    


while True:
    text = input("Enter a question: ")
    print(get_params(text))
    print()




"""
Date 
Partner         
Country 
Account - offline, online, overall
Dealer Type +
Coverage 
Location 
FEL AREA +
AREA  (Region sometimes)
Region 
Product Model 
CSM NAME 
FEL NAME 
ASM NAME 
REP NAME 
Store name +

"""













# top 10 stores perform in usa for last week in marysville
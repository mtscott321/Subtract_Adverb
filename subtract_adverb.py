# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 23:57:54 2020

@author: mtsco
"""

import io

adverbs = "adverbs.txt"

your_story = "your_story.txt"

#%%
all_adverbs = []
with open('adverbs.txt','r') as f:
    for line in f:
        for word in line.split():
           all_adverbs.append(word.lower()) 
         
#%%
symbols = []
with open("symbols.txt", 'r') as f:
    for line in f:
        for word in line.split():
            symbols.append(word)
#%%
your_words = []

with io.open(your_story, encoding="utf-8") as myfile:
    data = myfile.read()
    myfile.close()

words = data.split(" ")
for word in words:
    for symbol in symbols:
        word = word.replace(symbol, '')
        word = word.lower()
            
#%%
        
for i in range(0, len(words)):
    for adverb in all_adverbs:
        if words[i] == adverb:
            print("YOU HAVE AN ADVERB: %s" % (words[i]))
            
            
            
            
            
    
    
    
    
    
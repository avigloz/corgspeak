import json
import re

#* Wipe existing output dict. file in working directory
open('corgspeak_dict.json').close()

dictionary = open('dict.txt', 'r')
outputFile = open('corgspeak_dict.json', 'w')

data = {}

def getNewWord(word, mult=1, index=-1):
    if (index == -1):
        return word * mult
    return word[:index] * mult

def removeEscapes(word):
    escapes = word.find('\r\n')
    if (escapes == -1):
        pass
    else:
        word = word[:word.find('\r\n')]
    return word

for word in dictionary:
    word = removeEscapes(word)
    if (word == 'corgi'):
        data[word] = getNewWord(word, 2, 4)
        continue
    elif (word == 'julia'):
        data[word] = getNewWord(word, 2, 2)
        continue
    elif (len(word) <= 2):
        data[word] = word
    elif (len(word) > 2 and len(word) <= 4):
        data[word] = getNewWord(word, 2, 2)
    elif (len(word) >= 5):
        data[word] = getNewWord(word, 2, 3)

json.dump(data, outputFile)
print("corgcorg's dodo spespe!")
#? "corgi's done speaking!""

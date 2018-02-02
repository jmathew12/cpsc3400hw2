# James Mathew
# cpsc3400
# hw2-1.py

# import sys

def genLetters(input):
    input = input.lower()
    for x in input:
        if x.isalpha():
            yield x

x = input('enter a string: ')
letters = genLetters(x)
letterTable = {}
for letter in letters:
    if letterTable.get(letter) == None:
        letterTable[letter] = 1
    else:
        letterTable[letter] = letterTable[letter] + 1

genPairs = sorted(((i, letterTable.get(i)) for i in letterTable))
for i in genPairs:
    print (i)
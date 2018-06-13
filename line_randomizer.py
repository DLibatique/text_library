import random
from os import listdir
from cltk.tokenize.line import LineTokenizer

#initialize tokenizer
tokenizer = LineTokenizer('latin')

#create list of lines
whole_met = []

#iterate through files/books of Metamorphoses
for file in sorted(listdir('latin/ovid_metamorphoses')):

    #get text from each file
    with open('latin/ovid_metamorphoses/' + file) as f:
        raw = f.read()

    #add line-tokenized text to the master list of lines
    whole_met += tokenizer.tokenize(raw)

#test if there are any empty lines
def test_for_empty(list):

    #check for empty strings (which evaluate to False)
    if any in list is False:
        #get indices of empty strings
        print([i for i, x in enumerate(list) if x == ''])

    else:
        return 'No empty lines! Hooray!'

print(test_for_empty(whole_met))
#print(whole_met)
print(random.choice(whole_met))

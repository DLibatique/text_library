import random
import os
from cltk.tokenize.line import LineTokenizer

#initialize tokenizer
tokenizer = LineTokenizer('latin')

#create list of lines
whole_met = []

list_of_files = [file for file in listdir('la') if os.path.isfile(os.path.join('la/',file))]
print(list_of_files)

'''
#iterate through files/books of Metamorphoses
for file in [file for file in listdir('la') if os.path.isfile(os.path.join('la/',file))]:

    if file.startswith('ovid'):

        #get text from each file
        with open('la/' + file) as f:
            raw = f.read()

            #add line-tokenized text to the master list of lines
            whole_met += tokenizer.tokenize(raw)

            whole_met.replace('\t',' ')

#test if there are any empty lines
def test_for_empty(list):

    #check for empty strings (which evaluate to False)
    if any in list is False:
        #get indices of empty strings
        print([i for i, x in enumerate(list) if x == ''])

    else:
        return 'No empty lines! Hooray!'

print(whole_met)
'''

import random
from os import listdir

whole_met = []

for file in sorted(listdir('latin/ovid_metamorphoses')):

    with open('latin/ovid_metamorphoses/' + file) as f:
        raw = f.read()

    whole_met.extend(raw.split('\n'))

    for l in whole_met:
        if not l:
            whole_met.remove(l)

#test if there are any empty lines
def test_for_empty(list):

    if '' in list:

        print([i for i, x in enumerate(list) if x == ''])

    else:

        return 'No empty lines! Hooray!'

print(whole_met)

print(not whole_met[11996])
#print(random.choice(whole_met))

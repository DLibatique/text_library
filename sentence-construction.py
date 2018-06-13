import re
from os import listdir

txt_files = sorted(listdir('latin/ovid_metamorphoses'))
txt_files = [item for item in txt_files if item.endswith("txt")]

sent_count_pairs = []

for item in txt_files:

    infile = open('latin/ovid_metamorphoses/' + item)
    text = infile.read()
    infile.close()

    new_text = ""
    for l in text:

        added_text = str(l)

        new_text = new_text + added_text

        new_text = new_text.replace('\n',' ')

    sentences = re.split('[?!.;:]', new_text)

    word_count = {}

    for item in sentences:
        word_count[len(item.split())] = item

    sent_count_pairs.append(word_count)

for dict in sent_count_pairs:

    print(max(dict.keys()), dict[max(dict.keys())])

        # word_count_numbers.append(len(item.split()))

    # met_word_count_numbers.append(word_count_numbers)

# print(met_word_count_numbers)

# for list in met_word_count_numbers:
    # print(max(list))

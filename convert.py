from cltk.corpus.greek.beta_to_unicode import Replacer
import re
from os import listdir

r = Replacer()

#beta_files = sorted(listdir('homer_iliad/betacode_files'))
#text_files = [f for f in sorted(listdir('homer_iliad')) if f.endswith('txt')]
#zipped = zip(beta_files, text_files)

def clean_punc(text):

    punc = [r'&ldquo;', r'&rdquo;', r'&mdash;', r'&lsquo;', r'&rsquo;',
        r'&lsqb;', r'&rsqb;', r'&middot;', r'&iuml;', r'&euml;',
        r'&ouml;', r'&uuml;']
    uni = ['"', '"', '-', "'", "'", "[", "]", " · ", "ï", "ë", "ö", "ü"]
    combo = zip(punc,uni)

    for pair in combo:
        text = text.replace(pair[0],pair[1])

    return text

def convert_to_unicode(beta,text):

    #get text from betacode file
    infile = open(beta)
    raw = infile.read()
    infile.close()

    #remove &ldquo; &rdquo; and &mdash;
    raw = clean_punc(raw)
    raw = raw.split('\n')

    #convert text from beta to uni and put into list of lines
    full_text = [r.beta_code(line.upper().rstrip()) for line in raw]

    #open new text file, write converted line, close when finished
    file = open(text, 'w')
    for line in full_text:
        file.write(line + "\n")
    file.close()

    return full_text

#for pair in zipped:
    #convert_to_unicode('homer_iliad/betacode_files/' + pair[0], 'homer_iliad/' + pair[1])

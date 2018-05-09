import lxml.etree as ET
import re
from os import listdir
import convert

#list text files for the Iliad
txt_files = sorted(listdir('vergil_aeneid'))
txt_files = [item for item in txt_files if item.endswith("txt")]

parser = ET.XMLParser(recover=True)
tree = ET.parse('../../../../../cltk_data/latin/text/latin_text_perseus/Vergil/opensource/verg.a_lat.xml', parser=parser)
root = tree.getroot()

def check_type(r):
	if r.xpath('//div1[@type="Book"]'):
		return True

print(check_type(root))

#pair text file with proper book in the XML
zipped = list(zip(txt_files, root.xpath("//div1[@type='Book']")))

def write_to_txt(dir, pair):

	#open text file
	file = open(dir + '/' + pair[0],'w')

	#write lines associated with proper book to text file
	for l in pair[1].iter('l'):
		file.write(''.join(l.itertext()) + "\n")

	#close file
	file.close()

#write appropriate lines of each book to each text file
for x in zipped:
	write_to_txt('vergil_aeneid',x)

#convert HTML characters into unicode
for file in txt_files:

	#open and read each file
	infile = open('vergil_aeneid/' + file)
	text = infile.read()

	#conversion from &suchandsuch; to unicode symbol
	text = convert.clean_punc(text)

	#open and wipe each text file
	infile = open('vergil_aeneid/' + file, 'w')

	#write new text to file
	for l in text.split('\n'):
		infile.write(l + '\n')

	#close file
	infile.close()

for file in txt_files:

	infile = open('vergil_aeneid/' + file)
	text = infile.read()
	infile.close()

	for l in text.split('\n'):
		if '&' in l:
			print(l)

import lxml.etree as ET
import re
from os import listdir
import convert

#list text files for the Iliad
txt_files = sorted(listdir('latin/ovid_fasti'))
txt_files = [item for item in txt_files if item.endswith("txt")]

parser = ET.XMLParser(recover=True)
tree = ET.parse('../../../cltk_data/latin/text/latin_text_perseus/Ovid/opensource/ovid.fast_lat.xml', parser=parser)
root = tree.getroot()

#pair text file with proper book in the XML
if root.xpath("//div1[@type='Book']"):
	zipped = list(zip(txt_files, root.xpath("//div1[@type='Book']")))
elif root.xpath("//div1[@type='book']"):
	zipped = list(zip(txt_files, root.xpath("//div1[@type='book']")))

def write_to_txt(dir, pair):

	#open text file
	file = open(dir + '/' + pair[0],'w')

	#write lines associated with proper book to text file
	if pair[1].iter('l'):
		for l in pair[1].iter('l'):
			file.write(''.join(l.itertext()) + "\n")
	elif pair[1].iter('lb'):
		for l in pair[1].iter('lb'):
			file.write(''.join(lb.itertext()) + "\n")

	#close file
	file.close()

#write appropriate lines of each book to each text file
for x in zipped:
	write_to_txt('latin/ovid_fasti',x)

#convert HTML characters into unicode
for file in txt_files:

	#open and read each file
	infile = open('latin/ovid_fasti/' + file)
	text = infile.read()

	#conversion from &suchandsuch; to unicode symbol
	text = convert.clean_punc(text)

	#open and wipe each text file
	infile = open('latin/ovid_fasti/' + file, 'w')

	#write new text to file
	for l in text.split('\n'):
		infile.write(l + '\n')

	#close file
	infile.close()

for file in txt_files:

	infile = open('latin/ovid_fasti/' + file)
	text = infile.read()
	infile.close()

	for l in text.split('\n'):
		if '&' in l:
			print(l)

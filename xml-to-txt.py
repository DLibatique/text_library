import lxml.etree as ET
import re
from os import listdir

#list text files for the Iliad
txt_files = sorted(listdir('homer_odyssey'))

parser = ET.XMLParser(recover=True)
tree = ET.parse('../../cltk_data/greek/text/greek_text_perseus/Homer/opensource/hom.od_gk.xml', parser=parser)
root = tree.getroot()

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
	write_to_txt('homer_odyssey',x)

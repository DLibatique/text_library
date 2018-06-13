import urllib.request
from lxml import etree
import collections
import time
from pprint import pprint
from os import listdir

perseus_xml_base_url = "http://www.perseus.tufts.edu/hopper/xmlchunk?doc="

fasti_toc_url = "http://www.perseus.tufts.edu/hopper/xmltoc?doc=Perseus%3Atext%3A2008.01.0547%3Abook%3D1"

def check_for_books(root):

    if root.findall(".//chunk[@type='book']"):
        return True
    return False

with urllib.request.urlopen(fasti_toc_url) as f:
    perseus_toc_xml = f.read()

root = etree.fromstring(perseus_toc_xml)

if check_for_books(root):
    books = root.findall(".//chunk[@type='book']")
    booknames = [book.find('head').text for book in books]
else:
    books = [root]
    booknames = ['work']

book_refs = []

for book in books:
    if book.findall('chunk'):
        chunks = book.findall('chunk')
        refs = [chunk.attrib['ref'] for chunk in chunks]
        book_refs.append(refs)
    else:
        chunks = root.findall('chunk')
        refs = [chunk.attrib['ref'] for chunk in chunks]
        book_refs.append(refs)

book_sections = []

for book_ref in book_refs:
    book_section_xml = []
    for ref in book_ref:
        with urllib.request.urlopen(perseus_xml_base_url+ref) as f:
            book_section_xml.append(f.read())
    book_sections.append(book_section_xml)

def check_for_lb(root):
    """
    Some poetry in the Perseus XML has lines delimited by <lb>
    and some by <l>. This tests for the presence of <lb>, so that
    the right parser is used below.
    """
    if root.findall(".//lb"):
        return True
    return False

def node_text(node):
    """https://stackoverflow.com/a/7500304/1816347"""
    if node.text:
        result = node.text
    else:
        result = ''
    for child in node:
        if child.tail is not None:
            result += child.tail
    return result


# Get xml for each ref
book_lines = []

for section in book_sections:
    section_lines = []
    for xml in section:
        root = etree.fromstring(xml)

        if check_for_lb(root):
            lines = root.findall('.//lb')
            lines = [line.tail for line in lines]
            lines = ['\n' if line is None else line for line in lines]
            section_lines.append(lines)
        else:
            lines = root.findall('.//l')
            lines = [node_text(line) for line in lines]
            lines = ['\n' if line is None else line for line in lines]
            section_lines.append(lines)

    book_lines.append(section_lines)

for book in book_lines[0]:
    print(len(book))

txt_files = sorted(listdir('latin/ovid_fasti'))
txt_files = [item for item in txt_files if item.endswith("txt")]

zipped = list(zip(txt_files, book_lines[0]))

for (x,y) in zipped:
    file = open('latin/ovid_fasti' + '/' + x,'w')
    for l in y:
        file.write(l)
    file.close()

'''
def flatten(l):
    """https://stackoverflow.com/a/2158532/1816347"""
    for el in l:
        if isinstance(el, collections.Iterable) and not isinstance(el, (str, bytes)):
            yield from flatten(el)
        else:
            yield el

plaintext = flatten(book_lines)
print("\n".join(list(plaintext)))
'''

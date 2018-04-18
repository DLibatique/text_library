from cltk.corpus.greek.beta_to_unicode import Replacer
import re

test = r"""A)/NDRA MOI E)/NNEPE"""

r = Replacer()

print(r.beta_code(test))

'''
for line in open('homer_odyssey/hom_od_01.txt'):
    test = r'r\"\"\"' + line + r'\"\"\"'
    r = Replacer()
    print(r.beta_code(test))
'''

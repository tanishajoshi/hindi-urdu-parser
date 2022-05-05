from lark import Lark, Tree, Transformer
from lark.visitors import CollapseAmbiguities

my_grammar = """
start: np vp

np: det adj* n | det adj* n pp | adj* n  

vp: v np | v pp | v np pp

pp: prep np

det: "the" | "a" | "an"

n: "man" | "woman" | "telescope" | "waffles" | "British" | "left" | "Falklands"

v: "saw" | "left" | "waffles"

prep: "with" | "to" | "like" | "on" | "from"

adj: "big" | "little" | "old" | "young" | "British"

%import common.WS 
%ignore WS 
"""

parser = Lark(my_grammar, ambiguity='explicit')
corpus = """
the man saw the woman
the man saw the woman with the telescope
saw man the woman with the
the British left waffles on the Falklands
time flies like an arrow
the fruit flies like a banana
"""
for sent in corpus[1:].split('\n'):
  print("======\nsentence=",sent)
  try:
    parse_tree = parser.parse(sent)
    count = 0
    for x in CollapseAmbiguities().transform(parse_tree):
      print(x.pretty())
      count += 1
    print('Number of parses=',count)
  except:
    print('No valid parse.')

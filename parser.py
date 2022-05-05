from lark import Lark, Tree, Transformer
from lark.visitors import CollapseAmbiguities

my_grammar = """
start: subj obj vp

np: det adj* n | det adj* n pp | adj* n  

vp: v np | v pp | v np pp

pp: prep np

det: "ek" | "vo" | "ye" | "aur" | "na"

n: "aadmi" | "aurat" | "dhoorbeen" | "naan" | "Jatt" | "chali" | "daaktar" | "qismat"

v: "dekha" | "chali" | "karni" | "kheencho"

prep: "saath" | "ki" | "aise" | "par" | "pe" | "waise" | "jaise" | "se"

adj: "badaa" | "chota" | "budda" | "jawaan" | "Jatt"

adv: "kaise"

%import common.WS 
%ignore WS 
"""

parser = Lark(my_grammar, ambiguity='explicit')
corpus = """
mujhe aam pasand hain
vo khaana khaa raha hain
Ek aadmi paani peeraha hain
Ek aurat padrahi hain
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

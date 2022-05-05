from lark import Lark, Tree, Transformer
from lark.visitors import CollapseAmbiguities

my_grammar = """
start: np np* vp* cp*

cp: conj np vp*

np: det* adj* n | det adj* n pp | adj* n pp

vp: np v | v pp | v np pp | v adv

pp: prep np | prep

det: "ek" | "vo" | "ye" | "meri" | "us"

conj: "aur" | "lekin" | "ya" | "kyunki"

n: "aadmi" | "aurat" | "dhoorbeen" | "jhaad" | "chali" | "raste" | "tasveer" | "ladki" | "beti" | "daakter" | "ladka" | "chai" | "taare"

v: "dekhraha" | "chalraha" | "karni" | "kheencho" | "khadi" | "soti" | "shaadi" | "bhanaraha"

prep: "ke saath" | "ke uppar" | "aise" | "par" | "pe" | "ke paas" | "jaise" | "se" | "ke baad" | "ke piche"  

adj: "badaa" | "chota" | "budda" | "jawaan" | "naraaz" | "lambi" | 

adv: "kaise" | "hai" | "kareygi"

%import common.WS 
%ignore WS 
"""
parser = Lark(my_grammar, ambiguity='explicit')
corpus = """
ye ladki khadi hai
vo ladki jhaad ke piche khadi hai
ke piche khadi hai jhaad ladki vo 
ye naraaz ladki khadi hai aur aadmi chalraha hai lekin aurat soti hai
vo budda aadmi chalraha hai
meri beti daakter se shaadi kareygi
vo ladka chai bhanaraha hai
vo ladki dhoorbeen se taare dekhraha hai
meri beti us aurat ke saath tasveer kheencho
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

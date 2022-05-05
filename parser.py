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

n: "aadmi" | "aurat" | "dhoorbeen" | "jhaad" | "chali" | "raste" | "tasveer" | "ladki" | "beti" | "daakter" | "ladka" | "chai" | "taare" | "ghar" | "shaadi"

v: "dekhrahi" | "chalraha" | "chalrahi" | "karni" | "kheencho" | "khadi" | "soyi" | "shaadi" | "bhanaraha"

prep: "ke saath" | "ke uppar" | "aise" | "par" | "pe" | "ke paas" | "jaise" | "se" | "ke baad" | "ke piche" | "ko" | "mein"

adj: "badaa" | "choti" | "budda" | "jawaan" | "naraaz" | "lambi" | 

adv: "kaise" | "hai" | "kareygi"

%import common.WS 
%ignore WS 
"""
parser = Lark(my_grammar, ambiguity='explicit')
corpus = """
ye ladki khadi hai
vo ladki jhaad ke piche khadi hai
ke piche khadi hai jhaad ladki vo 
vo budda aadmi chalraha hai
meri beti daakter se shaadi kareygi
vo ladka chai bhanaraha hai
vo ladki dhoorbeen se taare dekhrahi hai
meri beti us aurat ke saath tasveer kheencho
vo lambi jhaad ke paas ek aurat raste ko dekhrahi hai
vo ghar mein shaadi chalrahi hai lekin ghar ke uppar choti beti soyi hai
"""
"""
Translated sentences:
This girl stands
That girl stands behind the tree
Behind stands the tree girl that
That old man is walking
My daughter will marry a doctor
That boy is making tea
That girl is looking at the stars through a telescope
Take a picture of my daughter with that woman
A woman near a tall tree looks at the street 
There is a wedding going on in that house but a girl sleeps above the house.
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

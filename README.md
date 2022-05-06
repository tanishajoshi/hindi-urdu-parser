# Hindi-Urdu Language Parser
## We utilize Lark (Python based) to build a basic human language parser
### Our parser does the following:
* Follows Hindi and Urdu grammar rules
* Follows Hindi and Urdu sentence structure
* Contains several sample sentences in the corpus for testing

Note: While the vocabulary of Urdu and Hindi are quite different, on the conversational level, they are quite similar and can be interchangeably spoken, hence we wanted to create 
this parser. Below we will explore some more rules of Hindi grammar and it's major differences
from English grammar.

## General Rules of Hindi Grammar
1. Grammar in Hindi follows the S-O-V order as opposed to S-V-O order used in English
2. Feminine and Masculine genders exist for all words
3. Multitude of ways to address other people (pronouns) that depend on the level of respect & formality given to them
4. Verb conjugation

For the purposes of this project, we have decided to not handle verb conjugation with the parser, as it can introduce a lot of complexity. 

Usage 
```
python3 parser.py
```
## Parser Sentence Structure
* The structure of a sentence in hindi is highly complex and variable
* For this use case, we go with a basic use case
* A sentence consists of np np* vp* cp* 
* I.E. a noun phrase followed by an optional number of noun phrases, verb phrases, and conjunctive phrases
* Conjunctive phrases consist of a conjunction noun phrase and an optional number of verb phrases.
* Noun phrases consist of determiners (in English commonly: a/an/the), while in Hindi/Urdu (ek/vo/ye/us/un), adjectives, nouns, and prepositional phrases
* Verb phrases can consist of noun phrases, verbs, prepositional phrases and adverbs 


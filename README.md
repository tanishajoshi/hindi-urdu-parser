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


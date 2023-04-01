import spacy 

nlp = spacy.load("en_core_web_sm")

txt_incorrect = nlp('Glade Candle Jar, Air Freshener, 2in1, Moonlit Walk & Wandering Stream, 3.4 Oz, 2 Count')

for token in txt_incorrect:
    print(token,'|',token.tag_, '|', spacy.explain(token.tag_))

print('---------------------------------------------------------------------')

txt_correct = nlp('Chesapeake Bay Candle PT41312 Scented Candle, Refresh + Rejuvenate (Mediterranean Citrus), Medium')

for token in txt_correct:
   print(token,'|',token.tag_, '|', spacy.explain(token.tag_))


'''
OUTPUT:
Glade | NNP | noun, proper singular
Candle | NNP | noun, proper singular <---
Jar | NNP | noun, proper singular
, | , | punctuation mark, comma
Air | NNP | noun, proper singular
Freshener | NNP | noun, proper singular
, | , | punctuation mark, comma
2in1 | CD | cardinal number
, | , | punctuation mark, comma
Moonlit | NNP | noun, proper singular
Walk | NNP | noun, proper singular
& | CC | conjunction, coordinating
Wandering | NNP | noun, proper singular
Stream | NNP | noun, proper singular
, | , | punctuation mark, comma
3.4 | CD | cardinal number
Oz | NN | noun, singular or mass
, | , | punctuation mark, comma
2 | CD | cardinal number
Count | NNP | noun, proper singular
---------------------------------------------------------------------
Chesapeake | NNP | noun, proper singular
Bay | NNP | noun, proper singular
Candle | NNP | noun, proper singular  <---
PT41312 | NN | noun, singular or mass
Scented | NNP | noun, proper singular
Candle | NNP | noun, proper singular
, | , | punctuation mark, comma
Refresh | NNP | noun, proper singular
+ | NNP | noun, proper singular
Rejuvenate | NNP | noun, proper singular
( | -LRB- | left round bracket
Mediterranean | NNP | noun, proper singular
Citrus | NNP | noun, proper singular
) | -RRB- | right round bracket
, | , | punctuation mark, comma
Medium | NN | noun, singular or mass
'''

import spacy 

nlp = spacy.load("en_core_web_sm")

txt_incorrect = nlp('Glade Candle Jar, Air Freshener, 2in1, Moonlit Walk & Wandering Stream, 3.4 Oz, 2 Count')
txt_correct = nlp('Chesapeake Bay Candle PT41312 Scented Candle, Refresh + Rejuvenate (Mediterranean Citrus), Medium')

for ent in txt_correct.ents:
    print(ent.text, '|', ent.label_, '|', spacy.explain(ent.label_))


print('---------------------------------------------------------------------')

for ent in txt_incorrect.ents:
    print(ent.text, '|', ent.label_, '|', spacy.explain(ent.label_))

'''
OUTPUT:
Chesapeake Bay Candle | PERSON | People, including fictional <---
---------------------------------------------------------------------
Glade Candle Jar | ORG | Companies, agencies, institutions, etc.  <---
Air Freshener | PERSON | People, including fictional
2in1 | DATE | Absolute or relative dates or periods
Moonlit Walk & Wandering Stream | ORG | Companies, agencies, institutions, etc.
3.4 Oz | PERCENT | Percentage, including "%"
2 | CARDINAL | Numerals that do not fall under another type
'''
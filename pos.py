import spacy 

nlp = spacy.load("en_core_web_sm")

txt_incorrect = nlp('Glade Candle Jar, Air Freshener, 2in1, Moonlit Walk & Wandering Stream, 3.4 Oz, 2 Count')

for token in txt_incorrect:
    print(token,'|',token.tag_, '|', spacy.explain(token.tag_))

print('---------------------------------------------------------------------')

txt_correct = nlp('Chesapeake Bay Candle PT41312 Scented Candle, Refresh + Rejuvenate (Mediterranean Citrus), Medium')

for token in txt_correct:
   print(token,'|',token.tag_, '|', spacy.explain(token.tag_))


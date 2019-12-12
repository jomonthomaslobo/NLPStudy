#Stemmer alogrithms are used generate various tense words by affix something 
from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize,word_tokenize
ps=PorterStemmer()
example_words=["python","pythoner","pythoning","pythoned","pythonly"]
for w in example_words:
    print(ps.stem(w))

print("---------------------------------------------")
new_text="able was i ere i saw elba"
words=word_tokenize(new_text)
for t in words:
    print(ps.stem(t))
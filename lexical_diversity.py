from __future__ import division
import nltk
from nltk.book import *

#function for searching lexical diversity .%ge of occurance of one word in
# a text is known as lexical diversity.Accepts text name returns diversity value
def find_lexical_diversity(text,word):
    lex_count  =text.count(word)/len(text)
    lex_percent=lex_count*100
    return lex_percent

def indexing_list():
    return text4.index('awaken')
    
print('--------------------------------')
text =["See" ,"you", "in", "Hell", "next"," month","you","can"]
print(find_lexical_diversity(text,text))
print(indexing_list())

#------------------------List --------------------------------------------------------

   

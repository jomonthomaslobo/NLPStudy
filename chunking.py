#Chunking
#combining parts of speech tags with regular expressions  
#
# + = match 1 or more
# ? = match 0 or 1 repetitions.
# * = match 0 or MORE repetitions	  
# . = Any character except a new line
import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer
from nltk import draw

train_text= state_union.raw("2005-GWBush.txt")
sample_text=state_union.raw("2006-GWBush.txt")
custom_sentence_tokenizer=PunktSentenceTokenizer(train_text)
tokenized=custom_sentence_tokenizer.tokenize(sample_text)


def process_content():
    try:
        for i in tokenized[:5]:
            words = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words)
           # print(tagged)
            chunkGram = r"""Chunk: {<RB.?>*<VB.?>*<NNP>+<NN>?}"""
            chunkParser = nltk.RegexpParser(chunkGram)
            chunked = chunkParser.parse(tagged)
            chunked.draw()   
            print(chunked)
            for subtree in chunked.subtrees(filter=lambda t: t.label() == 'Chunk'):
                print(subtree)
  


    except Exception as e:
        print(str(e))

process_content()
# -*- coding: utf-8 -*-

#tokenizer is used for splitting words and sentences .
from nltk.tokenize import sent_tokenize, word_tokenize 
sentence ="Now I was listening. Peter explained what you’ve all probably long since learned: that this bill would let the government devise a list of websites that Americans weren’t allowed to visit."

print("=============================Sentence Tokenized===============================")
print(sent_tokenize(sentence))

print("=============================Word Tokenized    ====================")
print(word_tokenize(sentence))

from nltk.tokenize import sent_tokenize, word_tokenize
#from nltk.book import *
data = "കേരളത്തിലെ കോട്ടയം ജില്ലയിലുള്ള പട്ടണവും, താലൂക്കുമാണ്‌ ചങ്ങനാശ്ശേരി. പഴയ തെക്കുംകൂർ രാജ്യ തലസ്ഥാനവും, അതിനുശേഷം തിരുവിതാംകൂറിലെ വലിയ വ്യാപാരകേന്ദ്രവും[1] ആയിരുന്ന ചങ്ങനാശ്ശേരി പട്ടണം അഞ്ചുവിളക്കിന്റെ നഗരം എന്ന അപരനാമത്തിൽ അറിയപ്പെടുന്നു. [2] ചങ്ങനാശ്ശേരി നഗരം 13.50 ചതുരശ്ര കിലോമീറ്ററിൽ വ്യാപിച്ചുകിടക്കുന്നു. ഈ പ്രദേശം ചങ്ങനാശ്ശേരി നഗരസഭയുടെ കീഴിലാണ്‌. എം.സി റോഡിനരികിലായി സ്ഥിതിചെയ്യുന്ന ഈ നഗരം ഇന്ന് മധ്യകേരളത്തിലെ പ്രധാന വ്യാപാരകേന്ദ്രമാണ്. കേരളത്തിന്റെ നെല്ലറയായ കുട്ടനാടിന്റേയും ഹൈറേഞ്ചിലെ പ്രധാന സ്ഥലങ്ങളുടെയും മദ്ധ്യഭാഗത്തായി സ്ഥിതിചെയ്യുന്നതിനാൽ അരി, കുരുമുളക്‌, ഇഞ്ചി, ഏലം എന്നിവയുടെ വ്യപാരത്തിൽ മുൻപന്തിയിലാണ്‌. "
print("Word")
print(word_tokenize(data))
print("Sentence")
print(sent_tokenize(data))
phrases = sent_tokenize(data)
words = word_tokenize(data)
print("phrase")
print(phrases)
print("word")
print(words)

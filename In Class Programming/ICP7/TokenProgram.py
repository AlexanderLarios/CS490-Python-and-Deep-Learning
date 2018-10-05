from bs4 import BeautifulSoup
import urllib.request as urlreq
from nltk import ne_chunk, pos_tag, wordpunct_tokenize, trigrams
import nltk
from nltk.stem import PorterStemmer, WordNetLemmatizer


nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')
nltk.download('maxent_ne_chunker')
nltk.download('words')

# Parse the website data
def getTextData():
    link = "https://en.wikipedia.org/wiki/Python_(programming_language)"
    source = urlreq.urlopen(link).read()
    soup = BeautifulSoup(source, 'html.parser')
    text1 = soup.getText()
    file_out = open("webpage_text.txt", 'w')
    file_out.write(text1)

# Break the text down into tokens for sentences and for words
def Tokenize():
    file_in = open("webpage_text.txt", 'r')
    output = open("sentence_token.txt", 'w')
    output2 = open("word_token.txt", 'w')
    token_text = file_in.read()
    sentTokens = nltk.sent_tokenize(token_text)
    wordTokens = nltk.word_tokenize(token_text)

    for s in sentTokens:
        output.write(s + '\n')

    for word in wordTokens:
        output2.write(word + '\n')

    return wordTokens

# stem the words
def Stem(param):
    porterStem = PorterStemmer()
    output = open("stemmed_words.txt", 'w')
    for words in param:
        output.write(porterStem.stem(words) + '\n')

# lemmetize the words
def Lemmentizer(param):
    lm = WordNetLemmatizer()
    output = open("lemmentized_words.txt", 'w')
    for words in param:
        output.write(lm.lemmatize(words) + '\n')

# tag the words by part of speech
def POS_tag(param):
    output = open("POS_TAG.txt", 'w')
    for words in param:
        output.write(str(nltk.pos_tag(words)) + '\n')

# search for proper nouns/etc
def NER():
    file_in = open("webpage_text.txt", 'r')
    output = open("NER.txt", 'w')
    ner_text = file_in.read()
    for sentence in ner_text:
        output.write(str(ne_chunk(pos_tag(wordpunct_tokenize(sentence)))) + '\n')

# create trigrams (tuples of three nearby words)
def TriGramOut(param):
    output = open("trigram.txt", 'w')
    trigramTokens = trigrams(param)
    for item in sorted(set(trigramTokens)):
        output.write(str(item) + '\n')


# call all of the functions
getTextData()
words = Tokenize()
Stem(words)
POS_tag(words)
Lemmentizer(words)
NER()
TriGramOut(words)

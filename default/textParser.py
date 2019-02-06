import nltk
from stop_words import get_stop_words

# some definitions
stopWords = get_stop_words('en')  # list of stopwords/english PyPl
tokenizer = nltk.tokenize.RegexpTokenizer(r'\w+')  # regex tokenization

class TextParser:
    
    # removes stopwords from list of words
    def removeStopWords(self, words):
        words = [w for w in words if w not in stopWords]
        return words

    # returns tokenized words
    def tokenizeWords(self, words_str):
        words = str(words_str.lower())
        return tokenizer.tokenize(words)

    # consolidates all pre-processing for words
    def cleanText(self, words):
        parsed_words = self.tokenizeWords(words)
        parsed_words = self.removeStopWords(parsed_words)
        return parsed_words
    
    # transform list of words in one string
    def concatenateWords(self, words):
        text= ''
        for word in words:
            text+=word+' '
        return text
    
    #removing unwanted chars/trash from sentences as strings
    def removeASCIItrash(self, words):
        cwords = words.encode('ascii', 'ignore').decode("utf-8")
        return (cwords)
    
        
        
        
        
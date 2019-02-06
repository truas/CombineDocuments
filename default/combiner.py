#imports
import os
import time

#from
from stop_words import get_stop_words
from default.textParser import TextParser
en_stop = get_stop_words('en') # list of stopwords/english

#overall runtime start
start_time = time.monotonic()

class Combiner:
    #===============================================================================
    # Document Reading/Writing
    #===============================================================================
    def oneBigFileOutput(self, files, ofname):
        tp = TextParser()
        big_document = open(ofname, 'w+', encoding='utf-8')    
        for index, file in enumerate(files):
            logs = file.split(os.sep)
            if (index % 5000 ==0): print('Processing:: %s' %logs[len(logs)-1])
            text = self.readFile(file)
            text = tp.cleanText(text)
            text = tp.concatenateWords(text)
            big_document.write(text+'\n')
        big_document.close()   
    #creates one file with each line being a document in the files list
    
    #===============================================================================
    # Folder manipulation
    #===============================================================================
    def doclist_multifolder(self, folder_name):
        input_file_list = []
        for roots, dir, files in os.walk(folder_name):
            for file in files:
                file_uri = os.path.join(roots, file)
                #file_uri = file_uri.replace("\\","/") #uncomment if running on windows           
                if file_uri.endswith('txt'): input_file_list.append(file_uri)
        return input_file_list
    #creates list of documents in many folders
    
    def readFile(self, file_name):
        text = ""
        try:
            f = open(file_name, errors="ignore")
            text = f.read()
            f.close()
        except IOError:
            raise ("FAILED: Problem reading file: " + file_name)
        return text 
    #read file entirely
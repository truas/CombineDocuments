'''
Created on Oct 30, 2018

@author: terry
'''
# import
import logging
import sys
import os

# python module absolute path
pydir_name = os.path.dirname(os.path.abspath(__file__))
ppydir_name = os.path.dirname(pydir_name)

# python path definition
sys.path.append(os.path.join(os.path.dirname(__file__),os.path.pardir))


from default.combiner import Combiner
from default.commandLineInterface import CommandLine

#show logs
logging.basicConfig(
    format='%(asctime)s : %(levelname)s : %(message)s',
    level=logging.INFO)



# main program
if __name__ == '__main__':  
    params = CommandLine()
    comb = Combiner()
       
    # folder paths
    input_folder = params.input_folder
    output_folder = params.output_folder
 
    # in/ou relative location - #input/output/model folders are under synset/module/
    in_foname = os.path.join(ppydir_name, input_folder) 
    ou_foname = os.path.join(ppydir_name, output_folder)
    
    #===========================================================================
    # #===========================================================================
    # # IDE - Path Definitions
    # #===========================================================================
    # in_foname = 'C:/Users/terry/Documents/Datasets/ArXiv/output'
    # ou_foname = 'C:/Users/terry/Documents/Datasets/ArXiv/result.txt'
    #===========================================================================
    
    #Doc and File list
    doc_paths =  comb.doclist_multifolder(in_foname)
    comb.oneBigFileOutput(doc_paths, ou_foname)
   
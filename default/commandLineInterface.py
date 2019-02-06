import argparse

class CommandLine:
    input_folder = None
    output_folder = None
    
    def __init__(self):
        parser = self.commandLineParameters()
        args = parser.parse_args()
        self.input_folder = args.in_f
        self.output_folder = args.on_f
    #constructor for parameters

    def commandLineParameters(self):
        parser = argparse.ArgumentParser(description="Combine several documents in one single document")
        parser.add_argument('--input', type=str, action='store', dest='in_f', metavar='<folder>', required=True, help='input folder to read document(s)')
        parser.add_argument('--output', type=str, action='store', dest='on_f', metavar='<folder>', required=True, help='output folder to write document(s)')      
        return(parser)
    #parameter list for command line
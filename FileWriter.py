import os

class FileWriter: 
    
    def __init__(self):
        self.cwdir = os.getcwd()
        if not os.path.exists(self.cwdir + '\data'):
            os.makedirs(self.cwdir + '\data')
        
    
    def write_trial(self, trial): 
        print("writing trial")
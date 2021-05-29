import os

class FileWriter: 
    
    def __init__(self):
        self.cwdir = os.getcwd()
        self.datadir = self.cwdir + '\data'
        if not os.path.exists(self.datadir):
            os.makedirs(self.datadir)
        
    
    def write_trial(self, trial): 
        print("writing trial")
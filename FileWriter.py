import os
from psychopy import data

class FileWriter: 
    
    def __init__(self, part):
        self.cwdir = os.getcwd()
        self.datadir = self.cwdir + '\data\\'
        if not os.path.exists(self.datadir):
            os.makedirs(self.datadir)
        self.file_name = self.datadir + 'p%s_%s' %(part.participant_number, data.getDateStr())
        self.participant = part
        
    
    def write_trial(self, trial): 
        with open(self.file_name, 'a') as f: 
            f.write(trial.to_string() + "," + self.participant.to_string() + "\n")

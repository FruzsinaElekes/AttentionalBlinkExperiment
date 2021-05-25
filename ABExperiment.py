from ABTrialClass import ABTrial
import random

class ABExperiment:
    
    def __init__(self, config):
        self.config = config
        self.create_trial_list()
        
        
    def create_trial_list(self):
        T1_0, T1_1, T1_2, T1_3 = self.config["vars"]["T1_pos"]
        total = self.config["vars"]["total_trial_number"]
        x_present = [1] * int(total / 2) + [0] * int(total / 2)
        T1_positions = ([T1_0] * int(total/8) 
            + [T1_1] * int(total/8) 
            + [T1_2] * int(total/8) 
            + [T1_3] * int(total/8)) * 2
        T2_lags = self.config["vars"]["T2_lag"] * int(total / 8) + [None] * int(total / 2)
        combined = list(zip(x_present, T1_positions, T2_lags))
        random.shuffle(combined)
        self.trial_list = [ ABTrial(*item, self.config) for item in combined ]
        
        
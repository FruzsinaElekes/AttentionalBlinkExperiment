from ABTrialClass import ABTrial
import random

class ABExperiment:
    
    def __init__(self, participant, presenter, config):
        self.participant = participant
        self.presenter = presenter
        self.config = config
        self.trial_list = self.create_trial_list()
        
        
    def create_trial_list(self):
        T1_0, T1_1, T1_2, T1_3 = self.config["vars"]["T1_pos"]
        total = self.config["vars"]["total_trial_number"]
        x_present = [1] * int(total / 2) + [0] * int(total / 2)
        T1_positions = ([T1_0] * int(total/8) 
            + [T1_1] * int(total/8) 
            + [T1_2] * int(total/8) 
            + [T1_3] * int(total/8)) * 2
        T2_lags = self.config["vars"]["T2_lag"] * int(total / 8) + [None] * int(total / 2)
        corr_detection = [self.participant.yes_key if i == 1 else self.participant.no_key for i in x_present]
        combined = list(zip(x_present, T1_positions, T2_lags, corr_detection))
        random.shuffle(combined)
        return [ ABTrial(*item, self.config) for item in combined ]
        
    
    def run(self):
        self.presenter.create_visual_objects()
        
        for t, trial in enumerate(self.trial_list): 
            if t == 0:
                self.presenter.instruct_waitkey(self.config["inst"]["start_exp"])
            elif t == self.config["vars"]["total_trial_number"] / 2:
                self.presenter.instruct_waittime_thenkey(self.config["inst"]["break"], 60)

            self.presenter.present_stimuli(trial)
            self.presenter.identification_task(trial)
            self.presenter.detection_task(trial)
            self.presenter.blank()
            self.file_writer.write_trial(trial)

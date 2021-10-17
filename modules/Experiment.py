from modules.Trial import Trial
import random

class Experiment:
    
    def __init__(self, participant, presenter, file_writer, config):
        self.participant = participant
        self.presenter = presenter
        self.file_writer = file_writer
        self.config = config
        self.trial_list = self.create_trial_list()
        
        
    def create_trial_list(self):
        T1_0, T1_1, T1_2, T1_3 = self.config["vars"]["T1_pos"]
        total = self.config["vars"]["total_trial_number"]
        half, eighth = int(total/2), int(total/8)
        x_present = [1] * half + [0] * half
        T1_positions = ([T1_0] * eighth + [T1_1] * eighth + [T1_2] * eighth + [T1_3] * eighth) * 2
        T2_lags = self.config["vars"]["T2_lag"] * eighth + [None] * half
        corr_detection = [self.participant.yes_key if i == 1 else self.participant.no_key for i in x_present]
        combined = list(zip(x_present, T1_positions, T2_lags, corr_detection))
        random.shuffle(combined)
        return [Trial(i, *item, self.config) for i, item in enumerate(combined)]
        
    def instruct_if_needed(self, trial):
        if trial.trial_number == 0:
            start = self.config["inst"]["start_exp"].format(*self.config["vars"]["targets"])
            self.presenter.instruct_waitkey(start)
        elif trial.trial_number == self.config["vars"]["total_trial_number"] / 2:
            self.presenter.instruct_waittime_thenkey(self.config["inst"]["break"], 60)
    
    def run(self):
        self.presenter.create_visual_objects()

        for trial in self.trial_list: 
            self.instruct_if_needed(trial)
            self.presenter.present_stimuli(trial)
            self.presenter.identification_task(trial)
            self.presenter.detection_task(trial, self.participant.yes_key, self.participant.no_key)
            self.presenter.blank()
            trial.calculate_accuracy()
            self.file_writer.write_trial(trial)

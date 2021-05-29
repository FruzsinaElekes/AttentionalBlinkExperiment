import random

class ABTrial:
    
    def __init__(self, x_present, T1_position, T2_lag, corr_detection, config):
        self.x_present = x_present
        self.T1_position = T1_position
        self.T2_lag = T2_lag
        self.corr_detection = corr_detection
        self.config = config
        self.identification_ans = None
        self.detection_ans = None
        self.stream = self.create_stream()
        self.target = self.stream[self.T1_position]
        
    def create_stream(self):
        self.T1 = random.sample (self.config["vars"]["targets"], 1)[0]
        letters_fin = [x for x in self.config["vars"]["letters"] if x != self.T1]
        stream = random.sample (letters_fin, 20)
        stream[self.T1_position] = self.T1
        if self.x_present == 1:
            stream[self.T1_position + self.T2_lag] = "X"
        return stream
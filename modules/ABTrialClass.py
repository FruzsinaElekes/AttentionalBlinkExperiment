import random

class ABTrial:
    
    def __init__(self, num, x_present, T1_position, T2_lag, corr_detection, config):
        self.trial_number = num
        self.x_present = x_present
        self.T1_position = T1_position
        self.T2_lag = T2_lag
        self.corr_detection = corr_detection
        self.config = config
        self.identification_ans = None
        self.detection_ans = None
        self.stream = self.create_stream()
        
    def create_stream(self):
        self.T1 = random.sample (self.config["vars"]["targets"], 1)[0]
        letters_fin = [x for x in self.config["vars"]["letters"] if x != self.T1]
        stream = random.sample (letters_fin, 20)
        stream[self.T1_position] = self.T1
        if self.x_present == 1:
            stream[self.T1_position + self.T2_lag] = "X"
        return stream
        
    
    def to_string(self): 
        return "{},{},{},{},{},{},{},{},{}".format(
            self.trial_number,
            self.T1,
            self.T1_position,
            self.x_present,
            self.T2_lag,
            self.identification_ans,
            self.detection_ans,
            self.corr_detection,
            "".join(self.stream))
    
    
    def get_header(self): 
        return "trial_no,T1,T1_pos,x_present,T2_lag,ident_ans,det_ans,det_corr,stream"
    
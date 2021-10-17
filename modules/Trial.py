import random

class Trial:
    
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
        self.det_accuracy = None
        self.ident_accuracy = None
        
    def create_stream(self):
        self.T1 = random.sample (self.config["vars"]["targets"], 1)[0]
        letters_fin = [x for x in self.config["vars"]["letters"] if x != self.T1]
        stream = random.sample (letters_fin, 20)
        stream[self.T1_position] = self.T1
        if self.x_present == 1:
            stream[self.T1_position + self.T2_lag] = "X"
        return stream
    
    
    def calculate_accuracy(self):
        self.det_accuracy = int(self.detection_ans == self.corr_detection)
        self.ident_accuracy = int(self.identification_ans.upper() == self.T1)
    
    def to_string(self): 
        return "{},{},{},{},{},{},{},{},{},{}".format(
            self.trial_number,
            self.T1,
            self.T1_position,
            self.x_present,
            self.T2_lag,
            self.identification_ans,
            self.detection_ans,
            "".join(self.stream),
            self.ident_accuracy,
            self.det_accuracy)
    
    
    def get_header(self): 
        return "trial_no,T1_letter,T1_pos,T2_present,T2_lag,ident_ans,det_ans,stream,ident_accuracy,det_accuracy"
    
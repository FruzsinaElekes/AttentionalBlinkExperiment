import random

class ABTrial:
    
    def __init__(self, x_present, T1_position, T2_lag, config):
        self.x_present = x_present
        self.T1_position = T1_position
        self.T2_lag = T2_lag
        self.config = config
        self.create_stream()
        
    def create_stream(self):
        self.T1 = random.sample (self.config["vars"]["targets"], 1)[0]
        letters_fin = [x for x in self.config["vars"]["letters"] if x != self.T1]
        self.stream = random.sample (letters_fin, 20)
        self.stream[self.T1_position] = self.T1
        if self.x_present == 1:
            T2_location = self.T1_position + self.T2_lag
            self.stream[T2_location] = "X"
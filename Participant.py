
class Participant:
    
    def __init__(self, p_no):
        self.participant_number = p_no
        k1, k2 = config["vars"]["part_keys"]
        self.yes_key = k1 if pno % 2 == 1 else k2
        self.no_key = k2 if pno % 2 == 1 else k1
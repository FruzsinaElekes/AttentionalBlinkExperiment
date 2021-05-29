
class Participant:
    
    def __init__(self, p_no, k1, k2):
        self.participant_number = p_no
        self.yes_key = k1 if p_no % 2 == 1 else k2
        self.no_key = k2 if p_no % 2 == 1 else k1
        
    
    def to_string(self): 
        return f"{self.participant_number},{self.yes_key},{self.no_key}"
    
    def get_header(self):
        return "part_no,yes_key,no_key"
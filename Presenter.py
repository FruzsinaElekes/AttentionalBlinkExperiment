from psychopy import visual, gui

class Presenter: 
    
    def __init__ (self, config):
        self.config = config
        
        
    
    def give_instruction(self, text):
        pass
        
    def ask_for_participant_number(self):
        exp_info =  {'participant_number':''}
        dlg = gui.DlgFromDict(dictionary = exp_info, title = 'AB')
        while dlg.OK == False:
            dlg = gui.DlgFromDict(dictionary = exp_info, title = 'AB')
        return int(exp_info['participant_number'])
from psychopy import visual, gui

class Presenter: 
    
    def __init__ (self, config):
        self.config = config
    
    
    def create_window(self):
        self.myWin = visual.Window(
            size = self.config["vars"]["monitor_size"], 
            color = self.config["vars"]["backgr_color"], 
            fullscr = True, 
            units = self.config["vars"]["units"])
        self.myWin.winHandle.set_mouse_visible(False)
    
    
    def give_instruction(self, text):
        print("give inst")
    
    
    def ask_for_participant_number(self):
        exp_info =  {'participant_number':''}
        dlg = gui.DlgFromDict(dictionary = exp_info, title = 'AB')
        if dlg.OK == False:core.quit()
        return int(exp_info['participant_number'])
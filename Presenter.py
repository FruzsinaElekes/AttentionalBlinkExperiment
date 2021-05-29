from psychopy import visual, gui, core, event

class Presenter: 
    
    def __init__ (self, config):
        self.config = config
    
    
    def create_visual_objects(self):
        self.myWin = visual.Window(
            size = self.config["vars"]["monitor_size"], 
            pos = [0,0],
            color = self.config["vars"]["backgr_color"], 
            fullscr = True, 
            units = self.config["vars"]["units"])
        self.myWin.winHandle.set_mouse_visible(False)
        
        self.instructions = visual.TextStim(
            self.myWin, 
            wrapWidth = self.config["vars"]["wrap_width"], 
            height = self.config["vars"]["text_height"], 
            color = self.config["vars"]["text_color"], 
            text = "")
    
    
    def instruct_waitkey(self, text):
        self.instructions.setText(text)
        self.instructions.draw()
        self.myWin.flip()
        keys = []
        #while len(keys) == 0:
        keys = event.waitKeys(keyList = ['space', 'escape'])
        if keys[0] == 'escape':
            core.quit()
    
    
    def ask_for_participant_number(self):
        exp_info =  {'participant_number':''}
        dlg = gui.DlgFromDict(dictionary = exp_info, title = 'AB')
        if dlg.OK == False:core.quit()
        return int(exp_info['participant_number'])
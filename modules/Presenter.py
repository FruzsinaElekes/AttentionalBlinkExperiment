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
            
        self.letter = visual.TextBox(window=self.myWin, 
                         text=".",
                         font_size=self.config["vars"]["stim_size"],
                         font_color=self.config["vars"]["text_color"], 
                         size=(200,200),
                         pos=(0.0,0.0), 
                         units='pix',
                         grid_vert_justification='center',
                         grid_horz_justification='center',
                         )
        self.fix_cross = visual.TextBox(window=self.myWin, 
                        text='+',
                        font_size=self.config["vars"]["stim_size"],
                        font_color=self.config["vars"]["text_color"], 
                        size=(200,200),
                        pos=(0.0,0.0), 
                        units='pix',
                        grid_horz_justification='center',
                        grid_vert_justification='center',
                        )
    
    
    def instruct_waitkey(self, text):
        self.present_text(text)
        key = event.waitKeys(keyList = ['space', 'escape'])[0]
        self.should_quit(key)
    
    
    def instruct_waittime_thenkey(self, text, secs):
        self.present_text(text)
        core.wait(secs)
        self.instruct_waitkey(self.config["inst"]["press_space"])
    
    
    def present_text(self, text): 
        self.instructions.setText(text)
        self.instructions.draw()
        self.myWin.flip()


    def ask_for_participant_number(self):
        exp_info =  {'participant_number':''}
        dlg = gui.DlgFromDict(dictionary = exp_info, title = 'AB')
        if dlg.OK == False:core.quit()
        return int(exp_info['participant_number'])
        
        
    def present_stimuli(self, trial): 
        for bl in range (0, self.config["vars"]["fix"]):
            self.fix_cross.draw()
            self.myWin.flip()
        for z in range (0, len(trial.stream)):
            self.letter.setText(trial.stream[z])
            
            if z == trial.T1_position:
                self.letter.setFontColor(self.config["vars"]["target_color"])
            else:
                self.letter.setFontColor(self.config["vars"]["text_color"])
            
            for f in range (0, self.config["vars"]["letter_time"]):
                self.letter.draw()
                self.myWin.flip()
            
            for f in range (0, self.config["vars"]["ITI"]):
                self.myWin.flip()
    
    def identification_task(self, trial): 
        self.present_text(self.config["inst"]["identification"])
        event.clearEvents()
        keys = list(map(str.lower, self.config["vars"]["targets"])) + ['escape']
        trial.identification_ans = event.waitKeys(keyList = keys)[0]
        self.should_quit(trial.identification_ans)
    
    
    def detection_task(self, trial, yes, no): 
        self.present_text(self.config["inst"]["detection"].format(yes.upper(), no.upper()))
        event.clearEvents()
        trial.detection_ans = event.waitKeys(keyList = [yes, no, 'escape'])[0]
        self.should_quit(trial.detection_ans)
        
    
    def blank(self): 
        for b in range (0,90):
            self.myWin.flip()

    
    def should_quit(self, key): 
        if key == 'escape': core.quit()
    
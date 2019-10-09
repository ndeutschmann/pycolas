from IPython.display import display

class ProgressBar:

    def __init__(self, step=0, n_steps=None, bar_length = 20, process_name = "Progress",display_here=True):
        self.step=step
        self.n_steps=n_steps
        self.bar_length=int(bar_length)
        self.process_name = process_name
        if display_here:
            self.display_init()
        else:
            self.display = None

    def gen_string(self):
        if self.n_steps is None:
            step_nb = int(self.step*self.bar_length)
            percent = int(100*self.step)
        else:
            step_nb = int(self.step*self.bar_length/self.n_steps)
            percent =  int(100*self.step/self.n_steps)
            

        return "{PROCESS}: [{DONE}{TODO}] {PERCENT}%".format(PROCESS=self.process_name,DONE="="*step_nb,TODO=" "*(self.bar_length-step_nb),PERCENT=percent)

    def display_init(self):
        self.display=display(self.gen_string(),display_id=True)

    def __call__(self,step):
        if self.display = None:
            self.display_init()
        self.step = step
        self.display.update(self.gen_string())
#needs to be able to grab the current date and time 
#needs to be able to display the current task and time left on the task 
#need to be  able to save it to save and open so that you don't have to enter it each day.
# need to have a break time after each task. 
import datetime
import time
from tkinter import * 
from tkinter import ttk
import winsound

class Efficiency_Timer():

    def __init__(self, root):
        self.entry_value = StringVar(root, value='')
        self.entry_text =StringVar(root, value='')
        self.working_text = StringVar(root, value='')
        self.break_text = StringVar(root, value='')
        root.title("Efficiency Timer")
        root.geometry("300x300")
        root.resizable(width=False, height=False)
        style = ttk.Style()
        style.theme_use('xpnative')
        self.seconds = 0
        self.working = False
        self.minutes = 0
        self.work_complete = False 
        self.break_time = False
        self.main()


    def main(self):
        # setting the body of the window
        self.entry_text.set("Enter work duration in minutes")
        entry_label = ttk.Label(root, textvariable=self.entry_text, justify="left").grid(row= 1, column= 3)
        self.timer = ttk.Entry(root , textvariable=self.entry_value, width = 5)
        self.timer.grid(row=2, column=3)
        self.enter_button = ttk.Button(root, text="Start", command=self.start).grid(row=3, column=3)
        
          
        if self.break_time == True:
            self.entry_text.set("")
            self.break_text.set("Rest Time")
            break_label = ttk.Label(root, textvariable=self.break_text, justify="left").grid(row= 1, column= 3)
            self.enter_button = ttk.Button(root, text="Go on break", command=self.start_break).grid(row=6, column=3)
            root.update_idletasks()
        

    def start(self):
        timer_time = int(self.timer.get()) - 1
        self.minutes = timer_time
        self.work_complete = False
        self.working = True
        self.seconds = 59
        root.update_idletasks()
        self.countdown()
    
    def countdown(self):
        self.working_text.set("Keep Going")
        working_label = ttk.Label(root, textvariable=self.working_text).grid(row=8, column=3)
        root.update_idletasks()
        timer_time = int(self.timer.get()) - 1
        self.minutes = timer_time
        while self.working == True:
            if self.seconds < 10:
                print(f"{self.minutes}:0{self.seconds}")
                self.seconds -= 1 
                time.sleep(1)
                
                
                if self.minutes == 0 and self.seconds == 0:
                    for i in range(3):
                        winsound.Beep(800, 1000) 
                    self.break_time = True
                    self.working = False
                    self.work_complete = True
                    
                elif self.seconds == 0:
                    self.minutes -= 1 
                    self.seconds = 59
            else:
                print(f"{self.minutes}:{self.seconds}")
                self.seconds -= 1
                time.sleep(1)
        self.working_text.set("")
        root.update_idletasks()       
        self.main()

    def start_break(self):
        self.seconds = 59
        self.minutes = 0
        self.working = True
        while self.working == True:
            if self.seconds < 10:
                print(f"{self.minutes}:0{self.seconds}")
                self.seconds -= 1 
                time.sleep(1)
                
                if self.minutes == 0 and self.seconds == 0:
                    for i in range(3):
                        winsound.Beep(800, 1000)  
                    self.break_time == False
                    self.working = False
                    self.work_complete = False
                    
                elif self.seconds == 0:
                    self.minutes -= 1 
                    self.seconds = 59
            else:
                print(f"{self.minutes}:{self.seconds}")
                self.seconds -= 1
                time.sleep(1)
        self.break_text.set("")
        self.main()


root = Tk()
app = Efficiency_Timer(root)
root.mainloop()


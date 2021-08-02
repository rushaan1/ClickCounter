from kivy.lang import Builder
from kivy.properties import StringProperty
from kivymd.app import MDApp
from kivy.clock import Clock
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton

KV = """
Screen:
    MDLabel:
        text: "Clicks: "+app.counter
        pos_hint: {'x':.28,'y':.38}
        font_size: '25sp'
        
    Button:
        text: "Click Here"
        size_hint: (.57,.37)
        pos_hint: {'x':.165,'y':.27}
        on_press: 
            app.counter_update()
            app.time_updater()
            
    MDLabel:
        text: "Time: "+app.timer
        pos_hint: {'x':.48,'y':.38}
        font_size: '25sp'
        
    MDLabel:
        text: "CPS: "+app.cps
        pos_hint: {'x':.63,'y':.38}
        font_size: '25sp'
        
    Button:
        text: "Restart"
        size_hint: (.2,.1)
        pos_hint: {'x':.35,'y':.09}
        on_press: 
            app.restart()
    
"""

class ClickCounter(MDApp):
    dshown = False
    restarted = False
    time = 0
    count = 0
    fcount = 0
    clikspersecond = 0
    counter = StringProperty(str(count))
    timer = StringProperty(str(time))
    cps = StringProperty(str(clikspersecond))

    def time_update(self,dt):
        if self.time == 10:
            if self.cps != "0":
                return
            self.count/=10
            self.cps = str(self.count)
            interval.cancel()
            yay_button = MDFlatButton(text="Yay!",on_release=self.close_dialog)
            if self.fcount <= 15:
                self.dialog = MDDialog(title="Time's Up!",text=f"You clicked {self.counter} times with the speed of {self.cps} Clicks Per Second! \n That was way too slow buddy, better practice hard",size_hint=(0.7, 1), buttons=[yay_button])
                self.dialog.open()
                self.dshown = True
                return
            elif self.fcount <= 30:
                self.dialog = MDDialog(title="Time's Up!",text=f"You clicked {self.counter} times with the speed of {self.cps} Clicks Per Second! \n Thats kinda slow dude, practice more!",size_hint=(0.7, 1), buttons=[yay_button])
                self.dialog.open()
                self.dshown = True
                return
            elif self.fcount <=50:
                self.dialog = MDDialog(title="Time's Up!",text=f"You clicked {self.counter} times with the speed of {self.cps} Clicks Per Second! \n Decent Enough, Can be better though!",size_hint=(0.7, 1), buttons=[yay_button])
                self.dialog.open()
                self.dshown = True
                return
            elif self.fcount <= 75:
                self.dialog = MDDialog(title="Time's Up!",text=f"You clicked {self.counter} times with the speed of {self.cps} Clicks Per Second! \n Really Good! Keep it up!!",size_hint=(0.7, 1), buttons=[yay_button])
                self.dialog.open()
                self.dshown = True
                return
            elif self.fcount <= 100:
                self.dialog = MDDialog(title="Time's Up!",text=f"You clicked {self.counter} times with the speed of {self.cps} Clicks Per Second! \n Dayum! Das Super Fast Bro!",size_hint=(0.7, 1), buttons=[yay_button])
                self.dialog.open()
                self.dshown = True
                return
        self.time += 1
        self.timer = str(self.time)

    def counter_update(self):
        if self.time == 10:
            if self.dshown == False:
                return
            self.time = 0
            self.count = 0
            self.clikspersecond = 0
            self.counter = "0"
            self.timer = "0"
            self.cps = "0"
            interval.cancel()
            self.dshown = False
            self.restarted = True
            self.fcount = 0
            return
        self.count += 1
        self.fcount += 1
        self.counter = str(self.count)

    def time_updater(self):
        if self.restarted == True:
            self.restarted = False
            return
        if self.count == 0 or self.count == 1:
            global interval
            interval = Clock.schedule_interval(self.time_update, 1)
        else:
            return


    def restart(self):
        self.time = 0
        self.count = 0
        self.clikspersecond = 0
        self.counter = "0"
        self.timer = "0"
        self.cps = "0"
        self.restarted = False
        self.dshown = False
        self.fcount = 0
        interval.cancel()

    def close_dialog(self,obj):
        self.dialog.dismiss()

    def build(self):
        return Builder.load_string(KV)

ClickCounter().run()

from kivy.app import App
from kivy.core import text
from kivy.uix.widget import Widget
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.properties import (
    NumericProperty,
    StringProperty,
    ObjectProperty
)


import os, sys

p = os.path.abspath('..')
sys.path.insert(1, p)

from timetable import getNewActivity, Content


class TimeTableUI(Widget):
    def turnBack(self,instance):
        self.mainPopUp.dismiss()

    def addContents(self,instance):
        self.addedContents = []
        lay = GridLayout(rows = 5)
        lay.add_widget(Label(text = ""))
        boxL = BoxLayout(orientation = "horizontal")
        boxL.add_widget(Label(text = "Content Name:"))
        boxL.add_widget(TextInput(text = "", multiline = False, halign = "center"))
        lay.add_widget(boxL)
        boxL = BoxLayout(orientation = "horizontal")
        boxL.add_widget(Label(text = "Content Frequency:"))
        boxL.add_widget(TextInput(text = "", multiline = False, input_filter = "int", halign = "center"))
        lay.add_widget(boxL)
        lay.add_widget(Label(text = ""))
        but = Button(text = "Add",font_size = 20)
        but.bind(on_press = self.addCont)
        lay.add_widget(but)
        self.addContentPopup = Popup(title = "Add Content", content = lay)
        self.addContentPopup.open()

    def addCont(self,instance):
        contName = ""
        contFreq = ""
        for child in self.addContentPopup.content.children:
            if isinstance(child, BoxLayout):
                if len(child.children) == 2:
                    boxChildren = child.children
                    if boxChildren[1].text == "Content Name:":
                        contName = boxChildren[0].text
                    else:
                        contFreq = boxChildren[0].text
        self.addedContents.append(Content(contName,int(contFreq)))
        self.addContentPopup.dismiss()
        for child in self.addActivitypopup.content.children:
            if isinstance(child,Label) and isinstance(child,Button) == False:
                child.text = "[color=00FF00][size=15]Content added [b]successfully[/b][/size][/color]"

    def hidegui(self, gui=None):
        if gui.text == "Get New Activity":
            lbl = Label(text="[size=30][b]" + getNewActivity(
            ) + "[/b][/size]",markup=True)
            lay = GridLayout(rows=2)
            lay.add_widget(lbl)
            btn = Button(text="[size=20][b]Turn Back[/b][/size]",markup=True)
            btn.bind(on_press=self.turnBack)
            boxL = BoxLayout(orientation="vertical")
            boxL2 = BoxLayout(orientation="horizontal")
            boxL.add_widget(Label(text = ""))
            boxL.add_widget(btn)
            boxL.add_widget(Label(text = ""))
            boxL2.add_widget(Label(text = ""))
            boxL2.add_widget(boxL)
            boxL2.add_widget(Label(text = ""))
            lay.add_widget(boxL2)
            self.mainPopUp = Popup(title='New Activity', content=lay)
            self.mainPopUp.open()
        else:
            lay = GridLayout(rows=5,cols = 1)
            lay.add_widget(Label(text="",markup = True))
            box = BoxLayout(orientation="horizontal")
            box.add_widget(Label(text = "Activity Name:"))
            box.add_widget(TextInput(text='', multiline=False, halign="center"))
            lay.add_widget(box)
            box = BoxLayout(orientation="horizontal")
            box.add_widget(Label(text = "Activity Frequency:"))
            box.add_widget(TextInput(text='', multiline=False, halign = "center", input_filter = "int"))
            lay.add_widget(box)
            box = BoxLayout(orientation="horizontal")
            box.add_widget(Label(text = "Activity Type:"))
            #btn1 = ToggleButton(text='Male', group='sex',)
            #btn2 = ToggleButton(text='Female', group='sex', state='down')
            box.add_widget(TextInput(text='', multiline=False, halign = "center", input_filter = "int"))
            lay.add_widget(box)
            box = BoxLayout(orientation="horizontal")
            btn1 = Button(text="Add Content")
            btn1.bind(on_press = self.addContents)
            box.add_widget(btn1)
            lay.add_widget(box)
            btn2 = Button(text = "Add")
            btn2.bind(on_press = self.saveActivity)
            lay.add_widget(btn2)
            self.addActivitypopup = Popup(title='Add Activity', content=lay)
            self.addActivitypopup.open()

    def saveActivity(self,instance):
        pass

class TimeTableApp(App):
    def build(self):
        return TimeTableUI()

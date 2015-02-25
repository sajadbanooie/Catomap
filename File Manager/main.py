# -*- coding: utf-8 -*-

import kivy
kivy.require('1.8.0')

from kivy.app import App
from kivy.core.window import Window
from kivy.config import Config
from kivy.clock import Clock
from kivy.core.audio import SoundLoader

from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.checkbox import CheckBox
from kivy.uix.screenmanager import Screen, ScreenManager, NoTransition, WipeTransition, SlideTransition, SwapTransition
from kivy.lang import Builder
from kivy.graphics import Color, Ellipse, Line, Rectangle, Point
Builder.load_file('Main')
import os
file_list = os.listdir(os.path.dirname(__file__))


class File(BoxLayout):
    def __init__(self, *args, **kwargs):
        super(File, self).__init__(**kwargs)
        self.name = args[0]
        self.path = args[1]
        self.mode, self.ino, self.dev, self.nlink, self.fuid, self.gid, self.fsize, self.atime, self.mtime, self.ctime = os.stat(self.path + "\\" + self.name)
        self.check = CheckBox()
        self.check.bind(active=self.on_checkbox_active)
        self.add_widget(self.check)
        self.add_widget(Label(text=self.name))

    def on_checkbox_active(self, c, value):
        if value:
            self.parent.parent.parent.parent.selected.append(self)
            self.parent.parent.parent.parent.select()
        else:
            self.parent.parent.parent.parent.selected.remove(self)
            self.parent.parent.parent.parent.select()


class MainScreen(Screen):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        for f in file_list:
            self.ids.Grid.add_widget(File(f, os.path.dirname(__file__)))
        self.selected = []

    def select(self):
        s = 'Selected Files: '
        for i in self.selected:
            s += "<"+i.name+">"

        self.ids.Action.title = s


sm = ScreenManager()
sm.add_widget(MainScreen(name='main'))
sm.current = 'main'


class MainApp(App):
    def build(self):
        return sm

if __name__ == '__main__':
    MainApp().run()
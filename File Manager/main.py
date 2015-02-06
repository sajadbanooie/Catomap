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

from kivy.uix.popup import Popup
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

from kivy.uix.screenmanager import Screen, ScreenManager, NoTransition, WipeTransition, SlideTransition, SwapTransition
from kivy.lang import Builder
from kivy.graphics import Color, Ellipse, Line, Rectangle, Point
Builder.load_file('Main')


class MainScreen(Screen):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)

sm = ScreenManager()
sm.add_widget(MainScreen(name='main'))
sm.current = 'main'


class MainApp(App):
    def build(self):
        return sm

if __name__ == '__main__':
    MainApp().run()
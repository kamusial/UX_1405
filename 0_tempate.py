import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.graphics import Color
from kivy.graphics import Rectangle
from kivy.graphics import Line
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen


class MyApp(App):
    def build(self):
        return


if __name__ == "__main__":
    MyApp().run()
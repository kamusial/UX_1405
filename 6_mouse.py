import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty

class Touch(Widget):
    def on_touch_down(self, touch):
        print('Mysz wcisnieta',touch)

class My6App(App):
    def build(self):
        return Touch()


if __name__ == "__main__":
    My6App().run()
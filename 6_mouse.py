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
        print('Mysz wcisnieta',touch.pos)
        self.btn.opacity = 0.3
    def on_touch_move(self, touch):
        print('Ruch myszą', touch)
    def on_touch_up(self, touch):
        print('mysz odcisnieta',touch.spos)
        self.btn.opacity = 1


class My6App(App):
    def build(self):
        return Touch()


if __name__ == "__main__":
    My6App().run()
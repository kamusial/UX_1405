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


class Touch(Widget):
    def __init__(self, **kwargs):
        super(Touch, self).__init__(**kwargs)

        with self.canvas:
            Color(1, 0, 0, 0.7, mode='rgba')
            self.rect1 = Rectangle(pos=(200,100), size=(80,90))
            Color(0, 1, 0, 0.7, mode='rgba')
            self.rect2 = Rectangle(pos=(0,0), size=(80,300))
            Color(0, 0, 1, 0.7, mode='rgba')
            self.rect3 = Rectangle(pos=(400,300), size=(220,100))


    def on_touch_down(self, touch):
        print('Mysz wcisnieta',touch.pos)
        self.btn.opacity = 0.3
        self.rect1.pos = touch.pos
    def on_touch_move(self, touch):
        print('Ruch myszą', touch)
        self.rect2.pos = touch.pos
    def on_touch_up(self, touch):
        print('mysz odcisnieta',touch.spos)
        self.btn.opacity = 1


class My6App(App):
    def build(self):
        return Touch()


if __name__ == "__main__":
    My6App().run()
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty

class MyGrid(Widget):
    p_imie = ObjectProperty()
    p_nazw = ObjectProperty()
    p_wiek = ObjectProperty()

    def submit_pressed(self):
        print('przycisk wcisniety')
        imie = self.p_imie.text
        nazwisko = self.p_nazw.text
        wiek = self.p_wiek.text
        print(f'Czesc {imie} {nazwisko}, twoj wiek to {wiek}.')

    def erased_pressed(self):
        if self.p_imie.text:
            self.p_imie.text = ''
            self.p_nazw.text = ''
            self.p_wiek.text = ''
        else:
            print('imie nie moze byc puste')

class My4App(App):
    def build(self):
        return MyGrid()


if __name__ == "__main__":
    My4App().run()
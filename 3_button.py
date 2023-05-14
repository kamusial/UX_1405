import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button

class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
        self.cols = 1

        self.inside = GridLayout()
        self.inside.cols = 2

        self.inside.add_widget(Label(text="Imie:  "))
        self.imie = TextInput(multiline=False)
        self.inside.add_widget(self.imie)

        self.inside.add_widget(Label(text="Nazwisko:  "))
        self.nazwisko = TextInput(multiline=False)
        self.inside.add_widget(self.nazwisko)

        self.inside.add_widget(Label(text="wiek:  "))
        self.wiek = TextInput(multiline=False)
        self.inside.add_widget(self.wiek)

        self.add_widget(self.inside)

        self.submit = Button(text="Wyslij", font_size=40)
        self.submit.bind(on_press=self.submit_pressed)
        self.add_widget(self.submit)

        self.erase = Button(text="Czysc", font_size=40)
        self.erase.bind(on_press=self.erased_pressed)
        self.add_widget(self.erase)

    def submit_pressed(self, instance):
        print('przycisk wcisniety')
        imie = self.imie.text
        nazwisko = self.nazwisko.text
        wiek = self.wiek.text
        print(f'Czesc {imie} {nazwisko}, twoj wiek to {wiek}.')

    def erased_pressed(self, instance):
        self.imie.text = ''
        self.nazwisko.text = ''
        self.wiek.text = ''

class MyApp(App):
    def build(self):
        return MyGrid()


if __name__ == "__main__":
    MyApp().run()
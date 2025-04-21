from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class ClickCounterApp(App):
    def build(self):
        self.counter = 0

        layout = BoxLayout(orientation='vertical', padding=50, spacing=20)

        self.label = Label(text="Kliknięcia: 0", font_size=32)
        self.button = Button(text="Kliknij mnie", font_size=32, size_hint=(1, 0.5))
        self.button.bind(on_press=self.increment_counter)

        layout.add_widget(self.label)
        layout.add_widget(self.button)

        return layout

    def increment_counter(self, instance):
        self.counter += 1
        self.label.text = f"Kliknięcia: {self.counter}"

ClickCounterApp().run()

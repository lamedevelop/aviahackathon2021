import time
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout

from kivy.uix.label import Label
from kivy.lang import Builder
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import ScreenManager
from kivymd.app import MDApp


class MyApp(MDApp):

    def build(self):
        screen = Builder.load_file('app.kv')
        return screen

    def go_to_map(self, screen_manager: ScreenManager):
        screen_manager.transition.direction = 'right'
        screen_manager.current = 'map'

    def go_to_route(self, screen_manager: ScreenManager):
        screen_manager.transition.direction = 'left'
        screen_manager.current = 'route'

    def go_to_profile(self, screen_manager: ScreenManager):
        screen_manager.transition.direction = 'left'
        screen_manager.current = 'profile'

    def plus(self):
        self.root.ids['cool_img'].size[0] += 100
        self.root.ids['cool_img'].size[1] += 100
        self.root.ids['cool_img'].pos[0] -= 50
        self.root.ids['cool_img'].pos[1] -= 50

    def minus(self):
        self.root.ids['cool_img'].size[0] -= 100
        self.root.ids['cool_img'].size[1] -= 100
        self.root.ids['cool_img'].pos[0] += 50
        self.root.ids['cool_img'].pos[1] += 50

    def map_reset(self):
        self.root.ids['scatter'].scale = self.root.width/160
        self.root.ids['scatter'].center = 35, -15
        self.root.ids['scatter'].rotation = 0

    def run_ticket_scanner(self):
        self.root.ids['user_gate'].text += ' my cool text'
        self.root.ids['user_departure'].text += ' my cool text'

    def build_path(self):
        pass

    def call_help(self):
        layout = GridLayout(cols=1, padding=10)

        popupLabel = Label(text="Help is called successfully. \nPlease wait.")
        closeButton = Button(text="Ok!")

        layout.add_widget(popupLabel)
        layout.add_widget(closeButton)

        # Instantiate the modal popup and display
        popup = Popup(title='Help is on the way',
                      content=layout,
                      size_hint=(None, None), size=(self.root.width/1.5, self.root.height/3))
        popup.open()

        # Attach close button press with popup.dismiss action
        closeButton.bind(on_press=popup.dismiss)


MyApp().run()

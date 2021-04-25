from kivy.lang import Builder
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

    def run_ticket_scanner(self):
        pass

    def build_path(self):
        pass


MyApp().run()

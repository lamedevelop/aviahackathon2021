from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from kivymd.app import MDApp
import qr_code_reader

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
        step = 5
        self.root.ids['scatter'].scale += step
        # self.root.ids['cool_img'].size[0] += 100
        # self.root.ids['cool_img'].size[1] += 100
        # self.root.ids['cool_img'].pos[0] -= 50
        # self.root.ids['cool_img'].pos[1] -= 50

    def minus(self):
        step = 5
        if self.root.ids['scatter'].scale > step:
            self.root.ids['scatter'].scale -= step
        # self.root.ids['cool_img'].size[0] -= 100
        # self.root.ids['cool_img'].size[1] -= 100
        # self.root.ids['cool_img'].pos[0] += 50
        # self.root.ids['cool_img'].pos[1] += 50

    def map_reset(self):
        self.root.ids['scatter'].scale = self.root.width/160
        self.root.ids['scatter'].center = 35, -15
        self.root.ids['scatter'].rotation = 0

    def run_ticket_scanner(self):
        qr_code_reader.main(self)




MyApp().run()

from operator import pos
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.widget import Widget
from kivymd.app import MDApp
from kivy.uix.gridlayout import GridLayout
from kivy.graphics import Color, Rectangle


class MyApp(MDApp):

    coords_list = []

    def build(self):
        screen = Builder.load_file('app.kv')

        COLS, ROWS = 55, 75
        COEFF = 1.16

        layout = GridLayout(cols=COLS, rows=ROWS)
        widget = screen.ids['coords']

        for j in range(ROWS):
            row_widgets=[]
            for i in range(COLS):
                widget_elem = Widget()
                with widget_elem.canvas:
                    Color(1,1,1,0)
                    # Color(random.random(), random.random(), random.random(), 0.2)
                    widget_elem.pos[0] += i*COLS/33.2/COEFF + 10.5
                    widget_elem.pos[1] += j*ROWS/48.7/COEFF
                    Rectangle(pos=widget_elem.pos,
                              size=(widget_elem.width/COLS/COEFF,
                                    widget_elem.height/COLS/COEFF))
                row_widgets.append(widget_elem)
                layout.add_widget(widget_elem)
            self.coords_list.append(row_widgets)
        widget.add_widget(layout)
        self.coords_list = self.coords_list[::-1]
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
        pass

    def _clean_paint_route(self):
        for array_of_widgets in self.coords_list:
            for widget in array_of_widgets:
                    with widget.canvas:
                        Color(1,1,1,0)

    def paint_route(self, coords_list):
        self._clean_paint_route()
        for y, array_of_widgets in enumerate(self.coords_list):
            for x, widget in enumerate(array_of_widgets):
                if (x,y,) in coords_list:
                    widget.canvas.children[1]=Color(0,0,1,0.8)


MyApp().run()

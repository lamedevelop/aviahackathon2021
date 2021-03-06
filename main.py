import time

import cv2
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout

from kivy.uix.label import Label
from operator import pos
from kivy.lang import Builder
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.widget import Widget
from kivymd.app import MDApp
from kivy.uix.gridlayout import GridLayout
from kivy.graphics import Color, Rectangle
from pyzbar import pyzbar
from kivy_garden.zbarcam import ZBarCam

from path_find.navigator import Navigator

CURR_PATH = []
CURR_PATH_INFO = ''


class MyApp(MDApp):
    coords_list = []

    def build(self):
        screen = Builder.load_file('app.kv')

        COLS, ROWS = 55, 75
        COEFF = 1.16

        layout = GridLayout(cols=COLS, rows=ROWS)
        widget = screen.ids['coords']

        for j in range(ROWS):
            row_widgets = []
            for i in range(COLS):
                widget_elem = Widget()
                with widget_elem.canvas:
                    Color(1, 1, 1, 0)
                    widget_elem.pos[0] += i * COLS / 33.2 / COEFF + 10.5
                    widget_elem.pos[1] += j * ROWS / 48.7 / COEFF
                    Rectangle(pos=widget_elem.pos,
                              size=(widget_elem.width / COLS / COEFF,
                                    widget_elem.height / COLS / COEFF))
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
        self.root.ids['scatter'].scale += 1

    def minus(self):
        self.root.ids['scatter'].scale -= 1

    def map_reset(self):
        self.root.ids['scatter'].scale = self.root.width / 160
        self.root.ids['scatter'].center = 35, -15
        self.root.ids['scatter'].rotation = 0

    def build_path(self):
        navigator = Navigator()
        start_name = self.root.ids['start_point'].text
        end_name = self.root.ids['end_point'].text
        start_id = navigator.getPointIdByName(start_name)
        end_id = navigator.getPointIdByName(end_name)
        CURR_PATH, CURR_PATH_INFO = navigator.build_path(start_id, end_id)
        self.root.ids['route_label'].text = navigator.path_info_to_str(CURR_PATH_INFO, len(CURR_PATH))
        self.paint_route(CURR_PATH)

    def build_path_by_ticket(self, screen_manager: ScreenManager):
        navigator = Navigator()
        default_start_id = 0
        default_end_id = 10  # out 105-106
        CURR_PATH, CURR_PATH_INFO = navigator.build_path(default_start_id, default_end_id)
        self.root.ids['route_label'].text = navigator.path_info_to_str(CURR_PATH_INFO, len(CURR_PATH))
        self.paint_route(CURR_PATH)
        screen_manager.transition.direction = 'right'
        screen_manager.current = 'map'

    def call_help(self):
        layout = GridLayout(cols=1, padding=10)

        popupLabel = Label(text="Help is called successfully. \nPlease wait.")
        closeButton = Button(text="Ok!")

        layout.add_widget(popupLabel)
        layout.add_widget(closeButton)

        popup = Popup(title='Help is on the way',
                      content=layout,
                      size_hint=(None, None), size=(self.root.width / 1.5, self.root.height / 3))
        popup.open()
        closeButton.bind(on_press=popup.dismiss)

    def _clean_paint_route(self):
        for array_of_widgets in self.coords_list:
            for widget in array_of_widgets:
                widget.canvas.children[1] = Color(1, 1, 1, 0)

    def paint_route(self, coords_list):
        self._clean_paint_route()
        for y, array_of_widgets in enumerate(self.coords_list):
            for x, widget in enumerate(array_of_widgets):
                if (x, y,) in coords_list:
                    widget.canvas.children[1] = Color(0, 0, 1, 0.8)

    def run_ticket_scanner(self):
        camera = cv2.VideoCapture(0)
        ret, frame = camera.read()
        while ret:
            ret, frame = camera.read()
            frame = self.read_barcodes(frame)
            cv2.imshow('Barcode/QR code reader', frame)
            if cv2.waitKey(1) == 27:
                ret = False
        camera.release()
        cv2.destroyAllWindows()

    def read_barcodes(self, frame):
        barcodes = pyzbar.decode(frame)
        for barcode in barcodes:
            x, y, w, h = barcode.rect
            barcode_info = barcode.data.decode('utf-8')
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, barcode_info, (x + 6, y - 6), font, 2.0, (255, 255, 255), 1)
            barcode_info = barcode_info.split()
            self.root.ids['user_gate'].text = 'Gate: ' + barcode_info[0]
            self.root.ids['user_departure'].text = 'Departure: ' + barcode_info[1]
        return frame


MyApp().run()

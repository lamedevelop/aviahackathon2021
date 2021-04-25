from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from kivymd.app import MDApp
import cv2
from pyzbar import pyzbar
from kivy_garden.zbarcam import ZBarCam


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
        camera = cv2.VideoCapture(0)
        if not camera.isOpened():
            print('Камера недоступна')
            return 0

        ret, frame = camera.read()
        # 2
        while ret:
            ret, frame = camera.read()
            barcode_info = self.read_barcodes(frame)
            cv2.imshow('Barcode/QR code reader', frame)

            if cv2.waitKey(1):
                break

            if len(barcode_info) > 6:
                ret = 0
        # 3
        camera.release()
        cv2.destroyAllWindows()

    def read_barcodes(self, frame):
        barcode = pyzbar.decode(frame)
        # x, y, w, h = barcode.rect
        # 1
        print(barcode)
        if len(barcode):
            barcode_info = barcode[0].data.decode('utf-8')
            self.root.ids['user_gate'].text = barcode_info
            return barcode_info
        #cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # 2
        # font = cv2.FONT_HERSHEY_DUPLEX
        # cv2.putText(frame, barcode_info, (x + 6, y - 6), font, 2.0, (255, 255, 255), 1)

        # self.root.ids['user_gate'].text = barcode_info

        # 3
        # with open("barcode_result.txt", mode='w') as file:
        #     file.write("Recognized Barcode:" + barcode_info)
        return 0


MyApp().run()

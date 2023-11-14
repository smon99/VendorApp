import time
from src.Core.GuiHandler import GuiHandler
from src.Core.CaptureScreen import CaptureScreen
from src.Core.OcrHandler import OcrHandler


class MarketController:

    def __init__(self):
        self.last_refresh = time.time()
        self.last_ocr_time = time.time()
        self.gui_handler_instance = GuiHandler()
        self.capture_screen_instance = CaptureScreen()
        self.ocr_handler_instance = OcrHandler()

    def process(self):
        while True:
            self.gui_handler_instance.click_refresh()
            time.sleep(1)
            screen = self.capture_screen_instance.capture_screen()
            price = self.ocr_handler_instance.perform_ocr(screen)
            time.sleep(10)
            print(price)

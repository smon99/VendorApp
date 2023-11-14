from PIL import ImageGrab


class CaptureScreen:

    @staticmethod
    def capture_screen():
        return ImageGrab.grab(bbox=(1350, 150, 1445, 190))

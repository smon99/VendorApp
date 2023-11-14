import pyautogui


class GuiHandler:

    @staticmethod
    def click_refresh():
        pyautogui.click(x=1837, y=120, clicks=1, button='left')

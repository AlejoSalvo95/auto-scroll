import pyautogui
import time

def start_scrolling(scroll_amount=-2, delay_between_scrolls=1):
    for _ in range(500):
        pyautogui.scroll(scroll_amount)
        time.sleep(delay_between_scrolls)

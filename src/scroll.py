import pyautogui
import time

def start_scrolling(scroll_amount=-2, scroll_times=200, delay_between_scrolls=1):
    for _ in range(scroll_times):
        pyautogui.scroll(scroll_amount)
        time.sleep(delay_between_scrolls)

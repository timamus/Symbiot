import pyautogui
import pyperclip
import time


def is_english_layout():
    # First, clear the input field
    pyautogui.hotkey('ctrl', 'a')
    time.sleep(0.5)
    pyautogui.press('delete')
    time.sleep(0.5)

    # Write a test string
    test_string = "test"
    pyautogui.write(test_string)
    time.sleep(0.5)

    # Select and copy the entered text
    pyautogui.hotkey('ctrl', 'a')
    time.sleep(0.5)
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(0.5)
    copied_text = pyperclip.paste()

    return copied_text == test_string


def ensure_english_layout():
    while not is_english_layout():
        # Switch the keyboard layout
        pyautogui.hotkey('alt', 'shift')
        time.sleep(0.5)

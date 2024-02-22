import pyautogui
import time
import datetime
import random
from random import randint

import keyboard_layout
import bezier_mouse_movement
from openai_helpers import fetch_openai_completion, extract_code_block


def type_like_a_human(text, duration, min_delay=0.05, max_delay=0.5, newline_delay=10, bracket_delay=10):
    """
    Function to simulate typing text like a human.

    :param text: the string of text to type
    :param duration: the total duration of the function in seconds
    :param min_delay: minimum delay between key presses
    :param max_delay: maximum delay between key presses
    :param newline_delay: maximum delay when moving to a new line
    :param bracket_delay: maximum delay after typing a bracket '('
    """
    start_time = time.time()

    # Move the cursor to the end of the document in most text editors
    pyautogui.hotkey('ctrl', 'end')
    time.sleep(1)

    while time.time() - start_time < duration and len(text) > 0:
        char = text[0]
        pyautogui.write(char)
        if char == '\n':
            time.sleep(random.uniform(0, newline_delay))
        elif char == '(':
            time.sleep(random.uniform(0, bracket_delay))
        else:
            time.sleep(random.uniform(min_delay, max_delay))

        text = text[1:]  # Remove the printed character from the text

    return text


def AI_symbiot_typer(api_key, prompt, hours):
    """
    Automates typing of OpenAI's ChatGPT responses in a text editor, mimicking human-like typing.

    Parameters:
    - api_key (str): OpenAI API key for ChatGPT requests.
    - prompt (str): Query or prompt for ChatGPT.
    - hours (int): Duration in hours for the function's operation.

    Functionality:
    The function waits 10 seconds before starting, allowing a switch to the target program. 
    It then enters a loop for the specified duration, fetching and typing out ChatGPT responses. 
    Typing simulates human patterns for realism.

    Note: Requires pyautogui, time modules, and functions for API communication and text extraction.
    """
    api_key = api_key
    prompt = prompt
    extracted_code = ""  # Initialize a variable to store text
    start_time_printed = False

    print("Waiting to switch to the required program in 10 seconds...")
    time.sleep(10)

    t_end = time.time() + 60 * 60 * hours
    while time.time() < t_end:
        # If the text has ended, request new one
        if not extracted_code:
            # Sending a request to ChatGPT
            print("Waiting for a response from ChatGPT...")
            chat_completion = fetch_openai_completion(api_key, prompt)
            # Retrieve the text content of the message
            chat_response = chat_completion.choices[0].message.content.strip()
            # Extract code from the text message
            extracted_code = extract_code_block(chat_response)

            # Check for the presence of code
            if extracted_code == "Code is not found":
                print(
                    "Error: Code not found in ChatGPT response. Terminating program execution.")
                print(chat_response)
                break  # Exit the loop, ending program execution

            # Check keyboard layout and set to English using Alt+Shift combination
            print("Checking the keyboard layout...")
            keyboard_layout.ensure_english_layout()

            # Deleting old text
            pyautogui.hotkey('ctrl', 'a')
            time.sleep(1)
            pyautogui.press('delete')
            time.sleep(1)

        # Determining the working time and break
        # Random work time between 10 to 30 minutes
        work_time = randint(10, 30) * 60
        # Random break between 8 to 14 minutes (more than 15 minutes might lock the RDP session)
        break_time = randint(8, 14) * 60

        if not start_time_printed:
            # Printing the start time of the work session
            start_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(f"Work session start time: {start_time}")
            start_time_printed = True

        # Printing the value in the console
        print(f"Work time: {work_time // 60} minutes ({work_time} seconds)")

        # Working for a specified time
        t_work_end = time.time() + work_time
        while time.time() < t_work_end and time.time() < t_end:
            # Typing text like a human with a random duration of 1 to 3 minutes
            type_like_a_human_duration = random.randint(60, 180)
            extracted_code = type_like_a_human(
                extracted_code, type_like_a_human_duration)
            # Moving the mouse and clicking with a random duration of 1 to 2 minutes
            random_mouse_move_duration = random.randint(60, 120)
            bezier_mouse_movement.random_mouse_move(
                200, 200, random_mouse_move_duration)

        print(f"Taking a break for {break_time/60} minutes.")
        time.sleep(break_time)

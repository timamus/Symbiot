# Symbiot

This Python script simulates human-like typing behavior to interact with text editors or IDEs. It's designed to work for extended periods, periodically generating and typing code based on responses from ChatGPT. The script includes features to ensure realistic typing patterns and mouse movements.

## Features
- **Human-like Typing**: Mimics real human typing with variable speed and pauses, including specific delays for new lines and brackets.
- **ChatGPT Integration**: Fetches code from ChatGPT using a given prompt and API key, ensuring a continuous supply of text to type.
- **Keyboard Layout Check**: Ensures the typing is always in the English layout, switching layouts if necessary.
- **Bezier Mouse Movement**: Simulates human-like mouse movements to maintain activity and realism.
- **Automated Work and Break Cycles**: The script operates in cycles of work and breaks, with durations varying randomly to enhance the human-like appearance.

## Requirements
- Python 3.x
- Libraries: `pyautogui`, `time`, `random`, `keyboard_layout`, `bezier_mouse_movement`, `openai_helpers`

## Usage
1. Set your OpenAI API key as an environment variable `OPENAI_API_KEY`. Detailed instructions can be found in our [installation guide](docs/OpenAI_Env_Setup.md).
2. Define your ChatGPT prompt.
3. Specify the duration for the script to run.

## Functionality
- **`type_like_a_human`**: Types the provided text over a given duration, imitating human typing behavior.
- **`AI_symbiot_typer`**: Main function that controls the flow of the script. It handles API requests, text extraction, and coordinates the typing and mouse movement.

## Quick start
- `sudo apt update && sudo apt install -y git`
- `git clone https://github.com/timamus/Symbiot.git`
- `cd Symbiot/`
- `find ./ -name "*.sh" -exec chmod +x {} \;`
- `python3 -m venv venv`
- `source venv/bin/activate`
- `pip install -r requirements.txt`
- `deactivate`

- **Linux Users**: Check if `xclip` is installed. This package is crucial for clipboard operations. You can verify its presence by running:
  
  ```bash
  xclip -version
  ```

  If `xclip` is not installed, install it using your distribution's package manager. For instance, on Ubuntu:

  ```bash
  sudo apt-get install xclip
  ```

## Creating a .desktop File
To create a `.desktop` file that will be accessible from your Linux distribution’s application menu, execute the following commands in the terminal:

```bash
# Ensure the necessary directory exists
mkdir -p ~/.local/share/applications/

# Create or overwrite the .desktop file with the content you provided
cat > ~/.local/share/applications/Symbiot.desktop << EOF
[Desktop Entry]
Name=Symbiot
Exec=$HOME/Symbiot/run_symbiot.sh
Icon=system-icon-name
Type=Application
Terminal=true
Categories=Utility;
EOF
```

This script first ensures that the ~/.local/share/applications/ directory exists. Then it creates or overwrites the Symbiot.desktop file in that directory with the content you specified. After executing these commands, "Symbiot" should be accessible from your application menu.

## Disclaimer
This script is intended for educational and experimental purposes only. Users are responsible for adhering to OpenAI's usage policies and any applicable software's terms of service.
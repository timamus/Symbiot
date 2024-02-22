# Setting Up the OPENAI_API_KEY Environment Variable

## For Linux Users

### Temporary Setup (Current Terminal Session Only)
1. Open your terminal.
2. Run the following command:
   ```
   export OPENAI_API_KEY='your_api_key'
   ```
   This sets the environment variable for the current session only.

### Permanent Setup
1. Open your terminal.
2. Add the export command to your shell's configuration file (`.bashrc` for Bash or `.zshrc` for Zsh):
   ```
   echo "export OPENAI_API_KEY='your_api_key'" >> ~/.bashrc
   ```
3. Apply the changes:
   ```
   source ~/.bashrc
   ```

## For Windows Users

### Temporary Setup (Current CMD/PowerShell Session Only)
1. Open Command Prompt or PowerShell.
2. Run the following command:
   ```
   set OPENAI_API_KEY=your_api_key
   ```
   This sets the environment variable for the current session only.

### Permanent Setup (Using GUI)
1. Press the Windows key and search for `env` or `environment variables`.
2. Select "Edit the system environment variables".
3. In the System Properties window, click on "Environment Variables".
4. Under "System Variables", click "New" and add `OPENAI_API_KEY` as the variable name and your API key as the value.

### Permanent Setup (Using Command Line)
#### Via Command Prompt
1. Open Command Prompt as an administrator.
2. Run the following command:
   ```
   setx OPENAI_API_KEY "your_api_key"
   ```
   Note: This updates the user-level environment variable. You may need to restart your Windows session for the changes to take effect.

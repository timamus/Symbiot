import os
from symbiot import AI_symbiot_typer


def main():
    api_key = os.environ.get("OPENAI_API_KEY")
    prompt = "Write an example of a corporate bank module code in C# with 100 lines"
    AI_symbiot_typer(api_key, prompt, 6)


if __name__ == "__main__":
    main()
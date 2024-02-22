from openai import OpenAI


def fetch_openai_completion(api_key, prompt):
    client = OpenAI(api_key=api_key)

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="gpt-3.5-turbo",
    )

    return chat_completion


def extract_code_block(chat_response):
    """
    Extracts a code block from the chat response.

    :param chat_response: The chat response containing the code block.
    :return: Extracted code block or a message indicating that the code is not found.
    """
    start_marker = "```"
    end_marker = "```"

    # Find the start and end of the code block
    start_index = chat_response.find(start_marker)
    end_index = chat_response.find(end_marker, start_index + len(start_marker))

    if start_index == -1 or end_index == -1:
        return "Code is not found"

    # Extract the code block
    # Find the next newline character after the start marker
    start_of_code = chat_response.find('\n', start_index)
    if start_of_code == -1:  # If newline is not found, start right after the marker
        start_of_code = start_index + len(start_marker)
    else:
        start_of_code += 1  # Start from the next character after newline

    code = chat_response[start_of_code:end_index].strip()
    return code

# Example usage
# chat_response = "Your chat response here"
# extracted_code = extract_code_block(chat_response)

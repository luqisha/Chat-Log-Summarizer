import re


def load_data(file_path='data/sample_chat.txt'):
    """
    Load data from a txt file into a string. [Req 1.1]

    Parameters:
    file_path (str): The path to the txt file.

    Returns:
    str: The content of the file as a string, or None if an error occurs.
    """
    try:
        with open(file_path, 'r', encoding="utf-8") as file:
            data = file.read()
        print(f"Data loaded successfully from {file_path}\n")
        return data
    except Exception as e:
        print(f"Error loading data: {e}\n")
        return None


def parse_chats(data):
    """
    Parse messages from chat data by speaker. [Req 2.1]

    Parameters:
    data (str): The chat data as a string.

    Returns:
    list: A list of dictionaries, each containing 'speaker' and 'message' keys.
            [
                {'speaker': 'User', 'message': 'Hello'},
                {'speaker': 'AI', 'message': 'Hi there'},
                ...
            ]
    """

    if not data:
        print("No data to parse.\n")
        return []

    split_data = re.split(r'(User:|AI:)', data)
    parsed_data = []

    if split_data[0] == '':
        split_data = split_data[1:]

    for i in range(0, len(split_data), 2):
        text = split_data[i].strip()

        if text == 'User:':
            parsed_data.append(
                {'speaker': 'User',
                 'message': split_data[i + 1].strip().replace('\n', ' ')
                 })
        elif text == 'AI:':
            parsed_data.append(
                {'speaker': 'AI',
                 'message': split_data[i + 1].strip().replace('\n', ' ')
                 })

    print(f"Parsed {len(parsed_data)} messages from chat data.\n")
    return parsed_data

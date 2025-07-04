import pandas as pd


def load_data(file_path='data/sample_chat.txt'):
    """
    Load data from a txt file into a string.

    Parameters:
    file_path (str): The path to the txt file.

    Returns:
    str: The content of the file as a string, or None if an error occurs.
    """
    try:
        with open(file_path, 'r', encoding="utf-8") as file:
            data = file.read()
        print(f"Data loaded successfully from {file_path}")
        return data
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

from utils.text_utils import load_data, parse_chats

chats = load_data()
parsed_chats = parse_chats(chats)
print(parsed_chats)

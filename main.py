import json
from utils.text_utils import load_data, parse_chats
from utils.chat_analyzer import get_message_stats, extract_keywords

chats = load_data()
parsed_chats = parse_chats(chats)
print(json.dumps(parsed_chats, indent=2), '\n')

message_stats = get_message_stats(parsed_chats)
print("Message Statistics: ", json.dumps(message_stats, indent=2), '\n')

top_keywords = extract_keywords(parsed_chats)
print("Top Keywords: ", top_keywords, '\n')

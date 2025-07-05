import json
from utils.text_utils import load_data, parse_chat
from utils.chat_analyzer import generate_summary, get_message_stats, extract_keywords

chats = load_data()
parsed_chats = dict()

for i, chat in enumerate(chats):
    print(f"Parsing chat {i+1}...")
    parsed_chats[f'chat_{i+1}'] = parse_chat(chat)
# print(json.dumps(parsed_chats, indent=2), '\n')

# message_stats = get_message_stats(parsed_chats)
# print("Message Statistics: ", json.dumps(message_stats, indent=2), '\n')

# top_keywords = extract_keywords(parsed_chats)
# print("Top Keywords: ", top_keywords, '\n')

# summary = generate_summary(parsed_chats)
# print(summary, '\n')

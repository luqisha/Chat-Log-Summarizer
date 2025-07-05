import json
from utils.text_utils import load_data, parse_chat
from utils.chat_analyzer import generate_summary, extract_keywords

chats = load_data()
parsed_chats = dict()

for i, chat in enumerate(chats):
    print(f"Parsing chat {i+1}...")
    parsed_chats[f'chat_{i+1}'] = parse_chat(chat)
# print(json.dumps(parsed_chats, indent=2), '\n')

top_keywords = extract_keywords(parsed_chats)
# print("Top Keywords: ", top_keywords '\n')
# print("Top Keywords: ", json.dumps(top_keywords, indent=2), '\n')

summary = generate_summary(parsed_chats)

for chat_id, chat_summary in summary.items():
    print(chat_summary)
    print("\n")

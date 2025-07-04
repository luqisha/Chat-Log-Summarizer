def get_message_stats(chat_data):
    """
    Get statistics of messages in the chat data. [Req 2.2]

    Parameters:
    chats (list): A list of dictionaries, each containing 'speaker' and 'message' keys.

    Returns:
    dict: A dictionary with statistics of messages.
          {
              'total_messages': int,
              'user_messages': int,
              'ai_messages': int,
          }
    """
    if not chat_data:
        print("No chats to analyze.\n")
        return {}

    total_messages = len(chat_data)
    user_messages = sum(
        1 for message in chat_data if message['speaker'] == 'User')
    ai_messages = total_messages - user_messages

    stats = {
        'total_messages': total_messages,
        'user_messages': user_messages,
        'ai_messages': ai_messages,
    }

    return stats

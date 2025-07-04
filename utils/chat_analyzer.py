import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


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


def extract_keywords(chat_data, k=5):
    """
    Extract top k keywords from a message by removing stop words and punctuation.
    [Req 2.3]

    Parameters:
    data (list): A list of dictionaries, each containing 'speaker' and 'message' keys.
    k (int): The number of top keywords to extract.

    Returns:
    list: A list of top k keywords.
    """
    if not chat_data:
        print("No data to extract keywords from.\n")
        return []

    nltk.download('punkt', quiet=True)
    nltk.download('stopwords', quiet=True)

    stop_words = set(stopwords.words('english'))
    word_corpus = []

    for data in chat_data:
        words = word_tokenize(data['message'])
        filtered_words = [word.lower() for word in words
                          if word.isalpha()
                          and word.lower() not in stop_words]
        word_corpus.extend(filtered_words)

    word_corpus.sort()

    freq_dist = nltk.FreqDist(word_corpus)
    top_keywords = [(freq, word) for word, freq in freq_dist.most_common(k)]

    return top_keywords

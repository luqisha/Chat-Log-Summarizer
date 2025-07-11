import nltk
from nltk.corpus import stopwords
from nltk.corpus import wordnet
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer


def get_message_stats(chat_data):
    """
    Get statistics of messages in the chat data. [Req 2.2]

    Parameters:
    chat_data (dict):   A dictionary with chat ID as keys and chat content as values.
                        The contents are structured as list of dictionaries, each item
                        containing 'speaker' and 'message' keys.

    Returns:
    dict:   A dictionary containing chat ID as keys and a dictionary of statistics as values.
            The statistics include:
                {
                    'total_messages': int,
                    'user_messages': int,
                    'ai_messages': int,
                }
    """

    if not chat_data:
        print("No chats to analyze.\n")
        return {}

    stats = dict()

    for chat_id, content in chat_data.items():
        total_messages = len(content)
        user_messages = sum(
            1 for message in content if message['speaker'] == 'User')
        ai_messages = total_messages - user_messages

        avg_message_length_user = 0
        if user_messages != 0:
            total_characters = sum(
                len(message['message']) for message in content if message['speaker'] == 'User')
            avg_message_length_user = round(total_characters / user_messages)

        avg_message_length_ai = 0
        if ai_messages != 0:
            total_characters = sum(
                len(message['message']) for message in content if message['speaker'] == 'AI')
            avg_message_length_ai = round(total_characters / ai_messages)

        chat_stats = {
            'total_messages': total_messages,
            'user_messages': user_messages,
            'ai_messages': ai_messages,
            'avg_message_length_user': avg_message_length_user,
            'avg_message_length_ai': avg_message_length_ai
        }

        stats[chat_id] = chat_stats

    return stats


def extract_keywords(chat_data, k=5):
    """
    Extract top k keywords from a message by removing stop words and punctuation.
    [Req 2.3]

    Parameters:
    chat_data (dict):   A dictionary with chat ID as keys and chat content as values.
                        The contents are structured as list of dictionaries, each item
                        containing 'speaker' and 'message' keys.
    k (int): The number of top keywords to extract.

    Returns:
    dict: A dictionary with chat IDs as keys and a list of tuples as values,
          where each tuple contains a keyword and its corresponding TF-IDF score.
    """

    if not chat_data:
        print("No data to extract keywords from.\n")
        return []

    nltk.download('punkt', quiet=True)
    nltk.download('stopwords', quiet=True)

    stop_words = set(stopwords.words('english'))
    documents = dict()

    # Process each chat to create a document for TF-IDF
    # Each document is a concatenation of all messages in the chat
    for chat_id, content in chat_data.items():
        chat_text = ' '.join([line['message'] for line in content])
        words = word_tokenize(chat_text)
        filtered_words = [word.lower() for word in words
                          if word.isalpha()
                          and word.lower() not in stop_words]

        documents[chat_id] = (' '.join(filtered_words))

    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(list(documents.values()))
    feature_names = vectorizer.get_feature_names_out()

    # Extract top k keywords for each chat
    top_keywords = {}
    for i, chat_id in enumerate(documents.keys()):
        # Get TF-IDF scores for current document
        tfidf_scores = tfidf_matrix[i].toarray()[0]

        # Create (score, word) pairs
        score_word_pairs = [(tfidf_scores[idx], feature_names[idx])
                            for idx in range(len(tfidf_scores))]

        # Sort by score desc first, then by word asc for ties
        score_word_pairs.sort(key=lambda x: x[1])
        score_word_pairs.sort(key=lambda x: x[0], reverse=True)

        # Get top k keywords
        top_keywords[chat_id] = score_word_pairs[:k]
    return top_keywords


def get_wordnet_pos(tag):
    """
    Convert POS tag to WordNet POS tag.

    Parameters:
    tag (str): POS tag from nltk.pos_tag.

    Returns:
    str: WordNet POS tag. 'N' for nouns, 'V' for verbs.
    """
    if tag.startswith('V'):
        return wordnet.VERB
    else:
        return wordnet.NOUN


def get_chat_nature(top_keywords):
    """
    Determine the nature of the chat.
    [Req 2.4]

    Parameters:
    keywords (dict):    A dictionary with chat IDs as keys and a list of tuples as values,
                        where each tuple contains a keyword and its corresponding TF-IDF score.

    Returns:
    dict:   A dict with chat IDs as keys and a string describing the nature of the chat.
            If no keywords are found for a chat, returns "Unknown".
    """

    if not top_keywords:
        return {}

    nltk.download('averaged_perceptron_tagger_eng', quiet=True)
    nltk.download('wordnet', quiet=True)
    nltk.download('omw-1.4', quiet=True)

    lemmatizer = WordNetLemmatizer()
    chat_nature = {}

    for chat_id, keyword_data in top_keywords.items():
        summary = str()

        keywords = [word for _, word in keyword_data]
        tagged_keywords = nltk.pos_tag(keywords)
        # print(tagged_keywords)

        lemmatized_keywords = [(lemmatizer.lemmatize(word, get_wordnet_pos(tag)), tag)
                               for word, tag in tagged_keywords]
        # print(lemmatized_keywords)

        verbs = [word for word,
                 tag in lemmatized_keywords if tag.startswith('V')]
        nouns = [word for word,
                 tag in lemmatized_keywords if tag.startswith('N')]

        summary = 'The user'
        if verbs:
            summary += f" discussed how to {', '.join(verbs)}"
        if nouns:
            summary += f" and focused on {', '.join(nouns)}"

        chat_nature[chat_id] = summary.strip()

    return chat_nature


def generate_summary(chat_data):
    """
    Generate a summary of the chat data. [Req 2.4]

    Parameters:
    chat_data (dict):   A dictionary with chat ID as keys and chat content as values.
                        The contents are structured as list of dictionaries, each item
                        containing 'speaker' and 'message' keys.

    Returns:
    dict:   Summary of each chat where each key is a chat ID and the value is a string 
            summarizing the chat.
    """

    if not chat_data:
        return "No data to summarize."

    summary = {}

    message_stats = get_message_stats(chat_data)
    top_keywords = extract_keywords(chat_data)
    chat_nature = get_chat_nature(top_keywords)

    for chat_id, _ in chat_data.items():
        if chat_id not in message_stats or chat_id not in top_keywords:
            continue

        top_keywords_str = ', '.join(
            [word for _, word in top_keywords[chat_id]])
        exchange_count = min(
            message_stats[chat_id]['user_messages'], message_stats[chat_id]['ai_messages'])

        summary_str = f"Summary for {chat_id}:\n" \
            + f"- The conversation contains {message_stats[chat_id]['total_messages']} messages in total.\n" \
            + f"- The conversation had {exchange_count} exchanges.\n" \
            + f"- User sent {message_stats[chat_id]['user_messages']} messages.\n" \
            + f"- AI sent {message_stats[chat_id]['ai_messages']} messages.\n" \
            + f"- Average message length of User is {message_stats[chat_id]['avg_message_length_user']} character.\n" \
            + f"- Average message length of AI is {message_stats[chat_id]['avg_message_length_ai']} character.\n" \
            + f"- {chat_nature[chat_id]}.\n" \
            + f"- Most common keywords: {top_keywords_str}."

        summary[chat_id] = summary_str

    return summary

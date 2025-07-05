# Chat-Log-Summarizer

This is a Python based tool that reads a chat log from a text file, parses the conversation, and produce a simple summary.

Features:

- Chat Log Parsing: Separates User and AI messages from formatted chat logs
- Message Statistics: Counts total exchanges and messages per speaker
- Keyword Extraction: Identifies top 5 most frequent keywords (excluding stopwords)

## 🔧 Setup

- Clone this repo using `git clone --single-branch --branch v1-single-chat https://github.com/luqisha/Chat-Log-Summarizer.git`
- Go to project directory using `cd Chat-Log-Summarizer`
- Install necessary dependencies using

  ```bash
  python -m venv venv
  venv\Scripts\activate
  pip install -r requirements.txt
  ```

## 🚀 Usage

- Place the chat log into `data/chat.txt` file. UTF-8 encoding is recommended. Each message should start with `User:` or `AI:`. Sample chat log looks like the following:

  ```
  User: Hi, can you tell me about Python?
  AI: Sure! Python is a popular programming language known for
  its readability.
  User: What can I use it for?
  AI: You can use Python for web development, data analysis,
  AI, and more.
  ```

- Run the tool using `python main.py` command in the terminal.

# Chat-Log-Summarizer

This is a Python based tool that reads chat logs dumped into [.txt] files, parses each conversation, and produce simple summary for each chat.

## ✨ Features

- Chat Log Parsing: Separates User and AI messages from formatted chat logs.
- Message Statistics: Provides the following message statistics:
  - Total number of messages
  - Number of exchanges (User-AI pairs)
  - Messages count per speaker
  - Average message length per speaker
- Keyword Extraction: Identifies top 5 most frequent keywords (excluding stopwords) for each chat using TF-IDF
- Chat summary: Generates a high-level summary of each chat's nature using POS tagging on the most frequent keywords.

## 📂 Project Structure

This project repository contains 3 branches.

- `main` branch contains the updated version that supports summarizing multiple chat logs from a folder and provides more detailed statistics.
- `v1-single-chat` branch contains a simple version of this tool that summarizes only a single chat log dumped to a specific text file, with fewer statistics.
- `dev` branch is the active development branch that contains work-in-progress changes.

## 🔧 Setup

- Clone this repo using `git clone --single-branch --branch main https://github.com/luqisha/Chat-Log-Summarizer.git`
- Go to project directory using `cd Chat-Log-Summarizer`
- Install necessary dependencies using

  ```bash
  python -m venv venv
  venv\Scripts\activate
  pip install -r requirements.txt
  ```

## 🚀 Usage

- Dump the chats into [.txt] files and put them on the `data/` directory.
- The text file must have UTF-8 encoding. File names can be anything, no specific naming convention required.
- Each message should start with `User:` or `AI:`. Sample chat log looks like the following:

  ```
  User: Hi, can you tell me about Python?
  AI: Sure! Python is a popular programming language known for
  its readability.
  User: What can I use it for?
  AI: You can use Python for web development, data analysis,
  AI, and more.
  ```

- Run the tool using `python main.py` command in the terminal.
- The script may take some time on the first run as it downloads required resources.

# 📂 Agentic File Search Assistant (LangChain + OpenAI)

The **Agentic File Search Assistant** is a hybrid AI tool that combines LLM reasoning with Python-based file search capabilities. Built using [LangChain](https://www.langchain.com/) and OpenAI GPT, this utility allows users to query folders in natural language and receive clean, intelligent summaries of files that match their keywords.

---

## 🧠 What It Does

- Accepts a natural prompt like _"Find files that contain the word 'invoice'"_
- Extracts the keyword using GPT
- Searches `.json`, `.txt`, and `.md` files in a target folder
- Returns a formatted list of matched file names using GPT

---

## 🛠 Tech Stack

- Python 3.9+
- [LangChain](https://docs.langchain.com/)
- [OpenAI GPT-3.5 Turbo](https://platform.openai.com/)
- Basic File I/O and `os` module for folder access

---


---

## 🚀 How to Run

### 1. Install Dependencies

```bash
pip install langchain openai


2. Set Your OpenAI API Key

export OPENAI_API_KEY="your-openai-key"


3. Create Sample Files
Create a folder named sample_files/ and add .json, .txt, or .md files containing searchable content.

python file_search_light.py


💻 Run the Script

python file_search_light.py



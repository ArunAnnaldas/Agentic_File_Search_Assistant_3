import os
from langchain.agents import Tool, initialize_agent
from langchain.chat_models import ChatOpenAI
from langchain.agents.agent_types import AgentType
from langchain.callbacks import get_openai_callback


def search_files_for_keyword(keyword: str) -> str:
    folder_path = "sample_files"
    keyword = keyword.lower()
    matched_files = []

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        if os.path.isfile(file_path) and filename.endswith((".json", ".txt", ".md")):
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
                try:
                    content = file.read().lower()
                    if keyword in content:
                        matched_files.append(filename)
                except Exception as e:
                    continue

    if not matched_files:
        return "No files found containing that keyword."
    return "Files found:\n" + "\n".join(matched_files)

# Define the tool
file_search_tool = Tool(
    name="FileSearch",
    func=search_files_for_keyword,
    description="Searches sample_files/ for text content. Input should be a single keyword to search in the files."
)

# LLM
llm = ChatOpenAI(temperature=0, 
	model_name="gpt-3.5-turbo",
	openai_api_key="",
	max_tokens=300

)

# Initialize agent
agent = initialize_agent(
    tools=[file_search_tool],
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=False
)

# Run a test query
with get_openai_callback() as cb:
    response = agent.run("Search for the word 'invoice' in files")
    print("🔍 Agent Response:\n", response)
    print(cb)
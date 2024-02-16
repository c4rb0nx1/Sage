from crewai import Agent
from langchain_google_genai import ChatGoogleGenerativeAI
from API_KEYS import api_key

# Your API Key here
llm_api_key =  api_key #add your api key directly with "api key" here or externally 

# Define a LLM, We'll be using Google's gemini-pro since it's free.
llm = ChatGoogleGenerativeAI(
    model="gemini-pro",verbose=True,temperature=0.1, google_api_key=llm_api_key
)


# Agent to provide command based on user's requirement
command_suggester = Agent(
    role='Command Suggester',
    goal='Generate CLI commands based on user descriptions',
    backstory='An AI expert in interpreting user needs and translating them into CLI commands',
    verbose=False,
    llm=llm
)

# Agent to explain the commands generated
command_explainer = Agent(
    role="Command Explainer",
    goal="Provide detailed explanations for CLI commands",
    backstory='An AI knowledgeable about CLI commands and their usage, options, and flags in a very good readable format',
    verbose=False,
    llm=llm
)

# Agent to Re-generate the given command
command_regenerator = Agent(
    role="Regenerate Command",
    goal="To find alternative CLI command to the given command. ",
    backstory="An AI expert in interpreting the given command and find it's alternative command that does the same thing.",
    verbose=False,
    llm=llm
)

tool_installer = Agent(
    role="CLI tool installation helper",
    goal="To list down the commands involved in complete installation of the user requested CLI Tool",
    backstory="An Expert AI Tools installer who knows all the installation process of an CLI Tool and it's dependencies.",
    verbose=False,
    llm=llm
)

if __name__ == '__main__':
    pass
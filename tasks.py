from crewai import Task
import agents as agents

# Tasks:
def generate_command(user_input):
    generate_command = Task(
        description = f'Generate a CLI command based on the user description:"{user_input}". Final answer MUST only be a valid command syntax.',
        agent=agents.command_suggester
    )
    return generate_command

def explain_command(user_input):
    explain_command = Task(
        description = f'Explain the given CLI command {user_input} in detail. Final answer MUST cover command usage, options and examples.',
        agent=agents.command_explainer
    )
    return explain_command

def regencommand(command):
    regenerate_command = Task (
        description=f"Regenerate alternative command based on the given command: {command}. make sure the command produced is accurate and solves the purpose of the given command.",
        agent=agents.command_regenerator
    )
    return regenerate_command

def tool_installer(tool_name):
    howto_command = Task(
        description = f"List all the necessary commands in order to install {tool_name}",
        agent=agents.tool_installer
    )
    return howto_command

if __name__ == '__main__':
    pass
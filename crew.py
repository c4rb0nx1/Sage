import os
import subprocess
import questionary
import agents as agents
import tasks as tasks
from crewai import Agent, Task, Process, Crew

# Setting the Crew to work.



# result of command suggester 
def GenC(user_input):
    crew1 = Crew(
    agents = [agents.command_suggester],
    tasks = [tasks.generate_command(user_input)],
    verbose=False,
    process=Process.sequential
    )
    GenC = crew1.kickoff()
    return GenC


def ExC(user_input):
    crew2 = Crew(
        agents = [agents.command_explainer],
        tasks = [tasks.explain_command(user_input)],
        verbose=False,
        process=Process.sequential
    )
    ExC = crew2.kickoff()
    return ExC

def regenerate(user_input):
    crew3 = Crew(
        agents = [agents.command_regenerator],
        tasks = [tasks.regencommand(user_input)],
        verbose=False,
        process=Process.sequential
    )
    RegC = crew3.kickoff()
    return RegC

def installer(tool_name):
    crew4 = Crew(
        agents = [agents.tool_installer],
        tasks = [tasks.tool_installer(tool_name)],
        verbose=False,
        process=Process.sequential
    )
    InS = crew4.kickoff()
    return InS

if __name__ == '__main__':
    pass
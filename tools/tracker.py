# Accepts updates, tracks user progress, modifies session contextfrom agents import funciton_tool
from agents import  Agent
from utils.utility_tools import context_updater
from utils.config import model



progress_tracker_tool = Agent(
    name="progres_tracker",
    instructions="You will access updates (progress) through user input to track user progress and update the user session context using <context_updater>",
    model=model,
    tools=[context_updater]
    
)
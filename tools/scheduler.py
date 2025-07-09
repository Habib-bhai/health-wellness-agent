# Schedules recurring weekly progress checks

from agents import Agent
from utils.config import model
from utils.utility_tools import context_updater, get_context


progress_check_scheduler = Agent(
    "progress_check_scheduler",
    instructions="""
    You will be checking users session that whether it is containing a progress or not using the <get_context> tool, if it got a progress check whether or not the progress_checking_date is assigned if not assign one, and when progress gets updated updated the progress_checking_date as well and assign a weekly date.
    """,
    model=model,
    tools=[context_updater, get_context]
)
# Converts user goals into structured format using input/output guardrails
# meaning it will be using the output_type of guardrails to convert the user input into a structured output.

from utils.config import model
from pydantic import BaseModel
from typing import Literal, Optional
from agents import Agent
from context import  UserSessionContext
from utils.utility_tools import context_updater
from guardrails import goal_structure_guardrail

goal_analyzer_agent =  Agent(
    name="goal_analyzer",
    instructions= "You will be checking users input that whether it is containing a goal or not with a quantity.",
    model=model,
    input_guardrails=[goal_structure_guardrail],
    tools=[context_updater]
)
    
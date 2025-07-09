# Async tool to suggest 7-day meal plan honoring dietary preferences
from agents import Agent, function_tool, RunContextWrapper
from utils.config import model
from context import UserSessionContext
from utils.utility_tools import context_updater


@function_tool
def user_session_info_provider(wrapper: RunContextWrapper[UserSessionContext]):
    return wrapper.context


meal_planner_tool = Agent(
    name="meal_planner",
    instructions="You are an expert meal planner, use <user_session_info> to access the user session context. You generate specific meal plans for the user analyzing the user session context (the user preferences in it). Update the user context using <context_updater) tool whenever u generate a meal plan for the user.",
    model=model,
    tools=[user_session_info_provider, context_updater]
)
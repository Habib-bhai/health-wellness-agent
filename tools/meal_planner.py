# Async tool to suggest 7-day meal plan honoring dietary preferences
from agents import Agent, function_tool, RunContextWrapper
from utils.config import model
from context import UserSessionContext


@function_tool
def user_session_info_provider(wrapper: RunContextWrapper[UserSessionContext]):
    return wrapper.context


meal_planner_tool = Agent(
    name="meal_planner",
    instructions="You are an expert meal planner, you create meals for the user fitness goal based analyzing their information present in the user session context (get the info using the user session tool)",
    model=model,
    tools=[user_session_info_provider]
)
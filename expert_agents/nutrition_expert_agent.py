# Complex dietary needs like diabetes or allergies
from agents import Agent
from utils.config import model
from tools.meal_planner import  meal_planner_tool


Nutrition_Expert = Agent(
    name="Nutrition_expert",
    instructions="You are an expert nutritionist, who collects necessary information from the user and guides them on nutrition and based on their nutrition requirements can also generate a 7 days meal plan for them using <meal_planner_tool>.",
    model=model,
    tools=[
        meal_planner_tool.as_tool(
        tool_name="meal_planner",
        tool_description="You are an expert meal planner, you generate specific meal plans for the user analyzing the user session context (the user preferences in it). "
    )]
)

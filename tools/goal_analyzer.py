# Converts user goals into structured format using input/output guardrails
# meaning it will be using the output_type of guardrails to convert the user input into a structured output.

from utils.config import model
from pydantic import BaseModel
from typing import Literal
from agents import Agent, Runner, function_tool, input_guardrail, GuardrailFunctionOutput, RunContextWrapper, TResponseInputItem
from context import  UserSessionContext

class GoalStructure(BaseModel):
    goal: str
    quantity : Literal["kg", "lbs"]
    is_a_goal: bool


input_formatter = Agent(
    name = "format input",
    instructions= "You will be checking users input that whether it is containing a goal or not, with a quantity.",
    output_type=GoalStructure,
    model=model
)

    
@input_guardrail
async def goal_structure_guardrail(ctx: RunContextWrapper[UserSessionContext], agent: Agent, input: str | list[TResponseInputItem] ) -> GuardrailFunctionOutput:
    """
    Converts user input into a structured goal format.
    """
    # print(agent.name) 
    
    result = await Runner.run(input_formatter, input, context=ctx.context)
    
    return GuardrailFunctionOutput(output_info=result.final_output, tripwire_triggered= not result.final_output.is_a_goal)   


@function_tool
def context_updater(wrapper: RunContextWrapper[UserSessionContext], goal, diet_preferences, workout_plan, meal_plan, injury_notes, handoff_logs, progress_logs ):
    """update the context object's properties goal, diet_preferences, workout_plan, meal_plan, injury_notes,handoff_logs, and progress_logs 
    
    Args:
        goal: user's fitness goal
        diet_preferences: user's diet preferences 
        workout_plan : workout plan generated for the user, by the workout recommender
        meal_plan: specific meal plan generated for the user based on his health activities, dietary preferences etc.
        injury_notes: Do user have any injuries etc. in past.
        handoff_logs: was there any handoffs done i.e. main agent handoff to any other agent for specific task.
        progress_logs: user's goal progress.
    """
    
    wrapper.context.goal = goal
    wrapper.context.diet_preferences = diet_preferences
    wrapper.context.workout_plan = workout_plan
    wrapper.context.meal_plan = meal_plan
    wrapper.context.injury_notes = injury_notes
    wrapper.context.handoff_logs = handoff_logs
    wrapper.context.progress_logs = progress_logs
    
goal_analyzer_agent =  Agent(
    name="goal_analyzer",
    instructions= "You will be checking users input that whether it is containing a goal or not with a quantity.",
    model=model,
    input_guardrails=[goal_structure_guardrail],
    tools=[context_updater]
)
    
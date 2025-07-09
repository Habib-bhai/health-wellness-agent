from pydantic import BaseModel
from typing import Optional, Literal
from agents import Agent,Runner, RunContextWrapper, TResponseInputItem, GuardrailFunctionOutput, input_guardrail
from context import UserSessionContext
from utils.config import model



class GoalStructure(BaseModel):
    goal: str
    quantity : Optional[Literal["kg", "lbs"]]
    is_a_health_goal: bool


input_formatter = Agent(
    name = "format input",
    instructions= "You will be checking users input that whether it is containing a health wellness goal or not, with a quantity (optional).",
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
    
    return GuardrailFunctionOutput(output_info=result.final_output, tripwire_triggered= not result.final_output.is_a_health_goal)   

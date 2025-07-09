from agents import function_tool, RunContextWrapper
from context import UserSessionContext


@function_tool
def get_context(ctx: RunContextWrapper[UserSessionContext]):
    return ctx.context


@function_tool
def context_updater(wrapper: RunContextWrapper[UserSessionContext], goal, diet_preferences, workout_plan, meal_plan, injury_notes, handoff_logs, progress_logs ):
    """update the context object's properties goal, diet_preferences, workout_plan, meal_plan, injury_notes,handoff_logs, and progress_logs 
    
    Args:
        goal: fitness goals of any type (lossing weight, gaining mass or any particular fitness level etc.)
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
    

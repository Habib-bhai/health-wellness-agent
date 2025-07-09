# Suggests workout plan based on parsed goals and experience

from agents import Agent 
from utils.config import model


workout_recommender_tool = Agent(
    name="workout_recommender",
    instructions="You are a workout recommending specialist.",
    model=model
)


    
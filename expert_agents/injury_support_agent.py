# Physical limitations or injury-specific workouts
from agents import Agent
from utils.config import model

injury_support = Agent(
    name="injury support",
    instructions="you will provide physical limitations and injury specific workouts if someone has any physical limitation or injury OR such history.",
    model=model
)

from utils.config import model
from agents import Agent, Runner, enable_verbose_stdout_logging,  set_tracing_disabled
from tools.goal_analyzer import goal_analyzer_agent, context_updater
from tools.meal_planner import meal_planner_tool
from context import UserSessionContext



set_tracing_disabled(disabled=True)
# enable_verbose_stdout_logging()

user_session_context = UserSessionContext(name="Habib", uid=29)


Health_wellness_agent = Agent(
    name="health_wellness_agent",
    instructions="You are a health and wellness agent. Your task is to assist users in achieving their health and wellness goals by providing personalized advice, meal plans, workout routines, and progress tracking. You will use the tools provided to help users with their specific needs. You will also handle any escalations to human coaches if necessary, injury support and nutrition expert advice (for that you've experts available that you can handoff to). Collect user fitness and dietary goals etc. through multi-turn natural language conversation. Use the context_updater tool to update the context object. use the meal planner tool to plan meals 7 days meal plan for the user.",
    model=model,
    tools=[goal_analyzer_agent.as_tool(
        tool_name="goal_analyzer", 
        tool_description="This tool will be analyzing user goal in the user input and give the output in structured form. ",
        ),
        context_updater,
        meal_planner_tool.as_tool(
            tool_name="meal_planner",
            tool_description="You are an expert meal planner, you generate specific meal plans for the user analyzing the user session context (the user preferences in it). "
        )   
        ],
    # handoffs=[]
)



history = []
while True:
    user_input = input("HI! I am health wellness agent, how can i help u ? use 'exit' to end the conversation: ")
    if user_input.lower() == "exit":
        break
    history.append({"role": "user", "content": user_input})        
    result = Runner.run_sync(Health_wellness_agent, history, context=user_session_context) 
    history = result.to_input_list() 
    
    
    print(result.final_output)
    print(result.input_guardrail_results)
    print("\n",user_session_context,"\n")
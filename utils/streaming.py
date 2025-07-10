from agents import Runner
from context import UserSessionContext
from agent import Health_wellness_agent
from openai.types.responses import ResponseTextDeltaEvent





async def main_streaming(user_input : str):
    user_session_context = UserSessionContext(name="Habib", uid=29)
    history = []
    history.append({"role": "user", "content": user_input})        
    result =  Runner.run_streamed(starting_agent=Health_wellness_agent,input=history, context= user_session_context) 
    history = result.to_input_list() 
    


    async for event in result.stream_events():
        if event.type == "raw_response_event" and isinstance(event.data, ResponseTextDeltaEvent):
            yield event.data.delta
            
    

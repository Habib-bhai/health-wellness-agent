from agents import Runner
from context import UserSessionContext
from agent import Health_wellness_agent
from openai.types.responses import ResponseTextDeltaEvent
import json




async def main_streaming(user_input : str):
    user_session_context = UserSessionContext(name="Habib", uid=29)
    history = []
    history.append({"role": "user", "content": user_input})        
    result =  Runner.run_streamed(starting_agent=Health_wellness_agent,input=history, context= user_session_context) 
    history = result.to_input_list() 
    


    async for event in result.stream_events():
        if event.type == "raw_response_event" and isinstance(event.data, ResponseTextDeltaEvent):
              yield json.dumps({
                "type": "text",
                "content": event.data.delta
            }) + "\n"
        
        elif event.type == "agent_updated_stream_event":
            # Adjust based on your actual event structure
            yield json.dumps({
                "type": "agent_handoff",
                "new_agent": event.new_agent.name,
                "message": f"Transferring to {event.new_agent.name} specialist..."
            }) + "\n"
            
    

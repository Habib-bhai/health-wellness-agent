# import chainlit as cl
# # from  agent.weather_agent import agent
# from agents import Runner, Agent
# from dotenv import load_dotenv
# from utils.config import model

# load_dotenv()



# agent = Agent(
#     name="assitant",
#     instructions="you are a helpfull assitant.",
#     model=model
# )


# @cl.on_chat_start
# async def chart_start():
#     cl.user_session.set("history" , [])
#     cl.user_session.set("agent" , agent)
#     await cl.Message(content=f"Welcome to the weather AI Assistant ! How may I help you").send()


# @cl.on_message
# async def on_mesg(message : cl.Message):
#     history = cl.user_session.get("history")
#     Agent = cl.user_session.get("agent")

#     msg = cl.Message(content="Thinking...")
#     await msg.send()

#     history.append({'role' : 'user' , 'content' : f'{message.content}'})

#     try:
#         print("\n[CALLING_AGENT_WITH_CONTEXT]\n", history, "\n")
#         result = await Runner.run(starting_agent=Agent , input=history)

#         response_content = result.final_output

#         msg.content = response_content
#         await msg.update()
        
#         # history.append({"role": "assistant", "content": response_content})
#         cl.user_session.set("history" , result.to_input_list())
#         # cl.user_session.set("history", history)
    

#         print(f"USER : {message.content}")
#         print(f"ASSITANT : {result.final_output}")


#     except Exception as e:
#         msg.content = f"Something went wrong please try again later."
#         await msg.update()
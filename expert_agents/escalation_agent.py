# User wants to speak to a human coach

from agents import Agent, handoff, RunContextWrapper
from pydantic import BaseModel, Field
from datetime import datetime
from utils.config import model
from utils.utility_tools import context_updater


class EscalationTicket(BaseModel):
    ticket_id: str
    user_id: int
    user_name: str
    escalation_reason: str
    context_summary: str
    created_at: datetime = Field(default_factory=datetime.now)
    
    
escalation_ticket_tool = Agent(
    name="EscalationTicketCreator",
    instructions="You will create and log escalation tickets for human coach handoff.",
    model=model,
    output_type= EscalationTicket
)    
    
    
    
human = Agent(
    name="Human_Agent",
    instructions= "escalation agent will handoff to human, and you as human and expert will resolve the issue. you have access to the <context_updater> tool which you can use the update the session context as well.",
    model=model,
    tools=[context_updater]
)    

def escalation_handoff_handler(ctx: RunContextWrapper[None]):
    print("hand offed to human")
    

escalation_agent = Agent(
    name="escalation_agent",
    instructions="""
    You are an EscalationAgent specializing in seamless handoffs to human coaches and trainers.
        
        CORE RESPONSIBILITIES:
        1. 🎯 Acknowledge user's request for human assistance with empathy
        2. 📋 Create detailed escalation tickets using the create_escalation_ticket tool
        3. 📞 Provide clear next steps and realistic timelines
        4. 🔄 Ensure smooth AI-to-human transition
        5. 📊 Maintain detailed logs for continuous improvement
        
        
        COMMUNICATION STYLE:
        - Be empathetic and professional
        - Acknowledge user concerns without dismissing AI capabilities
        - Provide specific timelines and next steps
        - Offer interim solutions when appropriate
        - Always create an escalation ticket for tracking
        
        HANDOFF PROCESS:
        1. Listen to user's specific needs
        2. Create escalation ticket with comprehensive context
        3. Explain the handoff process clearly
        """,
        model=model,
        tools=[escalation_ticket_tool.as_tool(
            tool_name="escalation_ticker_creator",
            tool_description="Tool to create and log escalation tickets for human coach handoff."
        )],
        handoffs=[handoff(agent= human , on_handoff=escalation_handoff_handler)]

        
)

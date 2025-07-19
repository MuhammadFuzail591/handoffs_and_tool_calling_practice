
from agents import Agent
from custom_agents.copywriting import copywriting_handoff
from custom_agents.summarizer import summarizer_handoff

lead_agent = Agent(
    name="Lead Agent",
    instructions=(
        "You are a marketing content director. Your job is to understand the user's goal and "
        "coordinate with your team of creative agents to produce the final content."
    ),
    handoffs=[copywriting_handoff, summarizer_handoff]
)

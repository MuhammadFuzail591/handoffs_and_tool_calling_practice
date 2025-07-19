
from agents import (Agent, handoff)

copywriting_agent = Agent(name="copywriting_expert")

copywriting_handoff = handoff(
    agent=copywriting_agent,
    tool_name_override="specialized_python_assistant",
    tool_description_override=(
        "You are a world-class copywriter. You write short, punchy, and persuasive text "
        "for ads and social media. You excel at creating catchy headlines and clear calls-to-action."
    )
)

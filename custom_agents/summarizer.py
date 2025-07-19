from agents import (Agent, handoff)

summarizer_agent = Agent(name="document_summarizing_agent")

summarizer_handoff = handoff(
   agent=summarizer_agent,
   tool_name_override="document_summarizing_expert",
   tool_description_override="You are a technical writer. Your skill is to read long, dense documents and extract the most important key facts and bullet points in a neutral, objective tone."
)
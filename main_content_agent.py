from agents import Runner
from rich import print

from custom_agents.lead_agent import lead_agent
from custom_agents.weather_agent import weather_agent
from config.openai_config import config

if __name__ == "__main__":
   result = Runner.run_sync(
      starting_agent=lead_agent,
      input="Hi there, what is your task and what you can do and what you have to accomplish your tasks.",
      run_config=config
   )

   print("Last Agent", result.last_agent)
   print("Result", result.final_output)
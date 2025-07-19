from agents import Runner
from rich import print

# from custom_agents.lead_agent import lead_agent
from custom_agents.weather_agent import weather_agent
from config.openai_config import config

if __name__ == "__main__":
   result = Runner.run_sync(
      starting_agent=weather_agent,
      input="Can you please tell me the tempreture of Lahore, Pakistan",
      run_config=config
   )

   # print("Last Agent", result.last_agent)
   print("Result", result.final_output)
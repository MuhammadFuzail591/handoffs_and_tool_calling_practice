from tools.get_weather_tool import fetch_weather
from agents import Agent


weather_agent = Agent(
   name = "Weather Assistant",
   instructions="You are a helpful weather assistant. When asked, use the get_weather tool to fetch current weather.",
   tools=[fetch_weather]
)





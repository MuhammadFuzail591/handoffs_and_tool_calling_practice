from agents import (function_tool)
import httpx


@function_tool
async def fetch_weather(city:str) -> str:
   """
      Fetch real weather data using wttr.in.

      Args: 
         city(str): Name of the city.
      
      Returns:
         str: Description of current weather and temperature.
      
   """
   try:
      async with httpx.AsyncClient(timeout=10) as client:
         resp = await client.get(f"https://wttr.in/{city}?format=%C+%t")
         resp.raise_for_status()

         return f"The weather in {city} is: {resp.text.strip()}"
   except Exception as e:
      return f"Error fetching Weather: {e}"
   
   
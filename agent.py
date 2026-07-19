# agent.py
def get_stadium_route(start_location: str, end_location: str, wheelchair_accessible: bool) -> str:
    """Returns the physical route between two points in the stadium."""
    if wheelchair_accessible:
         return f"To get from {start_location} to {end_location}, take the concourse to Elevator B."
    return f"To get from {start_location} to {end_location}, use Stairwell 3."

def get_live_wait_time(asset_name: str) -> str:
    """Returns the current live wait time or status for a stadium asset."""
    if asset_name == "Elevator B":
        return "Elevator B is currently experiencing a 15-minute delay due to heavy crowds."
    return f"{asset_name} is operating normally with no wait."
# agent.py (continued)
from google.antigravity import Agent, LocalAgentConfig

# Configure the agent
config = LocalAgentConfig(
    system_instructions="You are the official FIFA 2026 Multilingual Fan Concierge. You help fans navigate the stadium. Always use tools to check the physical route AND live wait times. Respond in the user's language.",
    tools=[get_stadium_route, get_live_wait_time],
    api_key="AQ.Ab8RN6Kw47cyDRFoRtTeR3iU253lWtRXLYVtK_iRNilkI_u0ZQ"
)

async def ask_concierge(fan_query: str) -> str:
    """Instantiates the agent and returns the text response."""
    # The Agent class manages the full lifecycle behind a single async context manager
    async with Agent(config) as agent:
        response = await agent.chat(fan_query)
        return await response.text()
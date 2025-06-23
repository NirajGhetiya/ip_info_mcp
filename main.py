from typing import Dict, Any
import httpx
from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("IPInfoServer")

# Constants
IPAPI_BASE = "https://ipapi.co"

@mcp.tool()
async def get_ip_info(ip_address: str) -> Dict[str, Any]:
    """
    Fetch geolocation information for a given IP address using ipapi.co.
    Args:
        ip_address: The IP address to query (e.g., '8.8.8.8').
    Returns:
        Dictionary containing IP information (e.g., city, country, latitude).
    """
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(f"{IPAPI_BASE}/{ip_address}/json/")
            response.raise_for_status()  # Raise an error for bad status codes
            return response.json()
        except httpx.HTTPStatusError as e:
            return {"error": f"Failed to fetch IP info: {str(e)}"}
        except httpx.RequestError as e:
            return {"error": f"Request error: {str(e)}"}

if __name__ == "__main__":
    mcp.run(transport="stdio")
# server.py
from mcp.server.fastmcp import FastMCP

# Create an MCP server
mcp = FastMCP("Demo")

# Add an addition tool
@mcp.tool()
def make_fart_noise(intensity_level: int) -> str:
    """Makes fart noise"""
    return f'p{intensity_level*"f"}t'

# Add a dynamic greeting resource
@mcp.resource("greeting://name")
def get_greeting() -> str:
    """Get a personalized greeting"""
    return f"Hello, name!"

def main():
    mcp.run('stdio')

if __name__ == "__main__":
    main()

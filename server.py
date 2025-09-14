import os
from mcp.server.fastmcp import FastMCP

# Set environment variables before creating FastMCP
os.environ["HOST"] = "0.0.0.0"
os.environ["PORT"] = "8000"

mcp = FastMCP("server")

@mcp.tool()
def greeting(name: str) -> str:
    "Send a greeting"
    return f"Hi {name}"

if __name__ == "__main__":
    mcp.run(transport="streamable-http")
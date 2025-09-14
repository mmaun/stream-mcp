from mcp.server.fastmcp import FastMCP
import uvicorn

mcp = FastMCP("server")

@mcp.tool()
def greeting(name: str) -> str:
    "Send a greeting"
    return f"Hi {name}"

if __name__ == "__main__":
    # Use uvicorn directly to control host/port
    uvicorn.run(mcp.app, host="0.0.0.0", port=8000)
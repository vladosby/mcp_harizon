from fastmcp import FastMCP
mcp = FastMCP("demo")

@mcp.tool()
def hello_world(name: str) -> dict:
    return f"Hello {name}!"

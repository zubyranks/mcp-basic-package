from mcp.server.mcpserver import MCPServer

mcp = MCPServer("Demo")


@mcp.tool()
def add(a: int, b: int) -> str:
    """Add two integers together and return a string."""
    return f"The sum of {a} and {b} is {a + b}"

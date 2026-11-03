from mcp.server.mcpserver import MCPServer

mcp = MCPServer("Demo")


@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two integers together and return a string."""
    return a + b

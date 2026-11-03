from mcp.server.mcpserver import MCPServer

mcp = MCPServer("Demo")


@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two integers together."""
    try:
        return a + b
    except Exception as e:
        raise ValueError(f"An error occurred while adding the numbers: {e}")

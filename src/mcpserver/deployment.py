from mcp.server.mcpserver import MCPServer

mcp = MCPServer("Demo")


@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two integers together."""
    try:
        return f"The sum is: {a} + {b}"
    except Exception as e:
        raise ValueError(f"An error occurred while adding the numbers: {e}")

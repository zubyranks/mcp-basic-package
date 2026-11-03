# MCP Basic Package

An MCP server with an `add` tool that adds two integers.

## Prerequisites

- [uv](https://docs.astral.sh/uv/) installed (provides the `uvx` command)

## Installation Guide

Add the following to your MCP client's config file (for example, Claude Desktop's `claude_desktop_config.json`):

```json
{
  "mcpServers": {
    "add_tool": {
      "command": "uvx",
      "args": [
        "--from",
        "git+https://github.com/zubyranks/mcp-basic-package.git",
        "mcpserver"
      ]
    }
  }
}
```

## Run the MCP Server from GitHub

```bash
uvx --from git+https://github.com/zubyranks/mcp-basic-package.git mcpserver
```

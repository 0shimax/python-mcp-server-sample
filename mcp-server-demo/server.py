from mcp.server.fastmcp import FastMCP

# Create an MCP server with debug enabled
mcp = FastMCP("Demo", debug=True)


# Add an addition tool
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


# Add this part to run the server
if __name__ == "__main__":
    # stdioトランスポートを使用
    print("Starting MCP server in stdio mode")
    mcp.run(transport="stdio")

### uvのインストール
```
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Pythonプロジェクトを作成
```
# mcp-server-demoというPythonプロジェクトを作成
uv init mcp-server-demo
```

### MCP SDKのインストール
```
# mcp-server-demoプロジェクト配下に移動
cd mcp-server-demo
# mcp-server-demoプロジェクトにmcp sdkをインストール
uv add "mcp[cli]"
```

### MCPサーバの構築
`server.py`ファイルの作成（ファイル名はなんでもよい）
```
mv main.py server.py
```

`server.py`に以下のように記述
```
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
```

### ClineへのMCPサーバの登録
ClineのプロジェクトMCPファイルを以下のように編集
```
{
  "mcpServers": {
    "mcp-demo-server": {
      "command": "uv",
      "args": [
        "--directory",
        <path to mcp-server-demo>,
        "run",
        "server.py"
      ],
      "alwaysAllow": [
        "add"
      ],
      "disabled": false
    }
  }
}
```
# MCP Math Agent

A Python MCP (Model Context Protocol) server that solves mathematical expressions and responds in Spanish. Designed for integration with VS Code Copilot.

## Features

- ✅ MCP-compliant server for VS Code Copilot integration
- ✅ Solves basic mathematical expressions (+, -, *, /, parentheses)
- ✅ Responds in Spanish (always)
- ✅ Safe expression evaluation with input validation
- ✅ Error handling for invalid expressions and division by zero
- ✅ Dual-language tool interface (Spanish and English tool names)

## Installation

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### As an MCP Server (for VS Code Copilot)

1. Start the MCP server:
   ```bash
   python mcp_server.py
   ```

The server runs in stdio mode and communicates using the MCP protocol. VS Code Copilot can use this server to answer math questions in Spanish.

### Available Tools

- **`calcular_matematicas`** - Tool with Spanish interface
- **`calculate_math`** - Tool with English interface

Both tools solve mathematical expressions and return results in Spanish.

### Example Tool Calls

**Spanish tool:**
```json
{
  "tool": "calcular_matematicas",
  "arguments": {
    "expresion": "2+2*3"
  }
}
```
Response: "La respuesta es: 8"

**English tool:**
```json
{
  "tool": "calculate_math", 
  "arguments": {
    "expression": "(10-5)*3+1"
  }
}
```
Response: "La respuesta es: 16"

### Legacy HTTP Server

The original Flask HTTP server is still available in `mcp_math_agent.py`:

```bash
python mcp_math_agent.py
```

Send POST requests to `http://localhost:8080/mcp`:
```json
{ "question": "2+2" }
```
Response:
```json
{ "answer": "La respuesta es: 4" }
```

## VS Code Copilot Integration

> 🚀 **Quick Setup**: For a streamlined setup process, see [VSCODE_SETUP.md](VSCODE_SETUP.md)

This section provides detailed instructions for integrating the MCP Math Server with VS Code Copilot.

### Prerequisites

1. **VS Code with Copilot**: Ensure you have VS Code with GitHub Copilot extension installed and active
2. **MCP Support**: VS Code must support MCP servers (available in recent versions)
3. **Python Environment**: Python 3.8+ with required dependencies installed

### Step-by-Step Setup

#### 1. Install Dependencies
```bash
cd mcp-math
pip install -r requirements.txt
```

#### 2. Configure VS Code for MCP

Create or update your VS Code MCP configuration file. The location depends on your operating system:

**Windows:**
```
%APPDATA%\Code\User\globalStorage\github.copilot-chat\mcpServers.json
```

**macOS:**
```
~/Library/Application Support/Code/User/globalStorage/github.copilot-chat/mcpServers.json
```

**Linux:**
```
~/.config/Code/User/globalStorage/github.copilot-chat/mcpServers.json
```

#### 3. Add Server Configuration

Add the following configuration to your `mcpServers.json` file:

```json
{
  "mcpServers": {
    "math-spanish": {
      "command": "python",
      "args": ["/absolute/path/to/mcp-math/mcp_server.py"],
      "env": {},
      "disabled": false,
      "alwaysAllow": ["calcular_matematicas", "calculate_math"]
    }
  }
}
```

**Important:** Replace `/absolute/path/to/mcp-math/mcp_server.py` with the actual absolute path to your `mcp_server.py` file.

#### 4. Restart VS Code

After adding the configuration, restart VS Code to load the new MCP server.

### Testing the Integration

#### 1. Verify Server Connection

Open VS Code and check if the MCP server is loaded:
1. Open Command Palette (`Ctrl+Shift+P` / `Cmd+Shift+P`)
2. Look for MCP-related commands or check the output panel for any MCP server errors

#### 2. Test with Copilot Chat

Open GitHub Copilot Chat in VS Code and try these examples:

**Spanish Math Questions:**
```
User: ¿Cuánto es 15 + 25?
Copilot: [Uses calcular_matematicas tool] La respuesta es: 40

User: ¿Qué es 7 multiplicado por 8?
Copilot: [Uses calcular_matematicas tool] La respuesta es: 56
```

**English Math Questions:**
```
User: What is (100-25) divided by 3?
Copilot: [Uses calculate_math tool] La respuesta es: 25.0

User: Calculate 2 + 2 * 3
Copilot: [Uses calculate_math tool] La respuesta es: 8
```

### How It Works

1. **Tool Discovery**: When VS Code starts, it connects to the MCP server and discovers available tools
2. **User Queries**: When you ask Copilot a math question, it recognizes the need for calculation
3. **Tool Selection**: Copilot chooses the appropriate tool (`calcular_matematicas` for Spanish context, `calculate_math` for English context)
4. **Execution**: The MCP server processes the mathematical expression safely
5. **Response**: Results are always returned in Spanish, as designed

### Available Tools

| Tool Name | Interface Language | Input Parameter | Description |
|-----------|-------------------|-----------------|-------------|
| `calcular_matematicas` | Spanish | `expresion` | Calculate mathematical expressions with Spanish interface |
| `calculate_math` | English | `expression` | Calculate mathematical expressions with English interface |

Both tools return results in Spanish regardless of the interface language.

### Supported Operations

- ✅ Addition (+): `2+3` → "La respuesta es: 5"
- ✅ Subtraction (-): `10-4` → "La respuesta es: 6"  
- ✅ Multiplication (*): `7*8` → "La respuesta es: 56"
- ✅ Division (/): `15/3` → "La respuesta es: 5.0"
- ✅ Parentheses: `(10+5)*2` → "La respuesta es: 30"
- ✅ Decimals: `3.14*2` → "La respuesta es: 6.28"
- ❌ Power operations (**): Blocked for security
- ❌ Complex functions: Only basic arithmetic supported

### Troubleshooting

**Server Not Loading:**
1. Check the absolute path in `mcpServers.json` is correct
2. Ensure Python can execute the script: `python /path/to/mcp_server.py`
3. Verify all dependencies are installed: `pip install -r requirements.txt`
4. Check VS Code output panel for error messages

**Tools Not Available:**
1. Restart VS Code after configuration changes
2. Verify the `alwaysAllow` permissions in configuration
3. Check that the MCP server starts without errors

**Copilot Not Using Tools:**
1. Make sure your questions are clearly mathematical
2. Try both Spanish and English phrasing
3. Ensure GitHub Copilot subscription is active

## Testing

Run the test script to verify functionality:
```bash
python test_mcp_server.py
```

The agent always responds in Spanish, regardless of the input language.

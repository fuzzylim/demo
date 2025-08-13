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

To integrate with VS Code Copilot, add this server to your MCP configuration. The server provides mathematical calculation capabilities in Spanish, allowing Copilot to solve math problems and respond appropriately in Spanish.

## Testing

Run the test script to verify functionality:
```bash
python test_mcp_server.py
```

The agent always responds in Spanish, regardless of the input language.

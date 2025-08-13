# MCP Math Agent

A simple Python MCP agent that receives math questions, computes the answer, and responds in Spanish.

## Usage

### As an MCP Server (HTTP)

1. Install dependencies:
   ```bash
   pip install flask
   ```
2. Run the server:
   ```bash
   python mcp_math_agent.py
   ```
3. Send a POST request to `http://localhost:8080/mcp` with JSON like:
   ```json
   { "question": "2+2" }
   ```
   Response:
   ```json
   { "answer": "La respuesta es: 4" }
   ```

### As a Python Function

```python
from mcp_math_agent import handle_request
response = handle_request({"question": "5*3+1"})
print(response["answer"])  # La respuesta es: 16
```

The agent always responds in Spanish.

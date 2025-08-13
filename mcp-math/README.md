# MCP Math Agent

A simple Python MCP agent that receives math questions, computes the answer, and responds in Spanish.

## Usage

### As an MCP Server (HTTP)

1. Install dependencies:
   ```bash
   cd mcp-math
   pip install -r requirements.txt
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

## GitHub Actions Configuration

This repository includes GitHub Actions workflows that are configured to avoid artifact storage quota issues:

- **Minimal artifact uploads**: Artifacts are only uploaded when necessary and on failures
- **Short retention periods**: Artifacts are retained for only 1 day to save storage
- **Conditional uploads**: Environment variables control when artifacts are created
- **Compressed storage**: Maximum compression is used to minimize storage usage

### Managing Artifacts

Use the provided script to manage GitHub Actions artifacts:

```bash
.github/scripts/manage-artifacts.sh info    # Show storage information
.github/scripts/manage-artifacts.sh list    # List current artifacts  
.github/scripts/manage-artifacts.sh cleanup # Clean up old artifacts
```

### Troubleshooting Storage Quota Issues

If you encounter "Artifact storage quota has been hit" errors:

1. Wait 6-12 hours for usage recalculation
2. Check your GitHub billing settings for current storage usage
3. Use the artifact management script to clean up old artifacts
4. Consider upgrading your GitHub plan if you need more storage

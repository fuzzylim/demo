# Quick VS Code Setup Guide

## 🚀 5-Minute Setup for VS Code Copilot

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 2: Find Your Configuration Path

**Copy the path for your operating system:**

| OS | Configuration File Path |
|---|---|
| **Windows** | `%APPDATA%\Code\User\globalStorage\github.copilot-chat\mcpServers.json` |
| **macOS** | `~/Library/Application Support/Code/User/globalStorage/github.copilot-chat/mcpServers.json` |
| **Linux** | `~/.config/Code/User/globalStorage/github.copilot-chat/mcpServers.json` |

### Step 3: Get Your Full Path
```bash
# Run this in the mcp-math directory to get the full path:
pwd
# Copy the output - you'll need it for the next step
```

### Step 4: Create/Edit Configuration File

Create or edit the `mcpServers.json` file with this content:

```json
{
  "mcpServers": {
    "math-spanish": {
      "command": "python",
      "args": ["REPLACE_WITH_YOUR_FULL_PATH/mcp_server.py"],
      "env": {},
      "disabled": false,
      "alwaysAllow": ["calcular_matematicas", "calculate_math"]
    }
  }
}
```

**Important:** Replace `REPLACE_WITH_YOUR_FULL_PATH` with the actual path from Step 3.

### Step 5: Restart VS Code

Close and reopen VS Code completely.

### Step 6: Test It!

Open GitHub Copilot Chat and try:

**Ask in English:**
```
What is 15 + 25?
```

**Ask in Spanish:**
```
¿Cuánto es 7 * 8?
```

Both should get responses in Spanish like "La respuesta es: 40" and "La respuesta es: 56".

## ✅ Verification

If it's working correctly:
- Copilot will use the math tools automatically for math questions
- All responses will be in Spanish
- You'll see calculation results, not just Copilot's built-in math knowledge

## 🛠️ Troubleshooting

**Problem: Tools not working**
1. Check the file path is absolute and correct
2. Test the server manually: `python mcp_server.py`
3. Check VS Code's Output panel for errors

**Problem: Copilot doesn't use the tools**
1. Make sure your questions are clearly mathematical
2. Try rephrasing: "Calculate X + Y" or "¿Cuánto es X + Y?"
3. Restart VS Code after configuration changes
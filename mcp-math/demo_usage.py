#!/usr/bin/env python3
"""
Example usage demonstration of the MCP Math Server
This shows how VS Code Copilot would interact with the server
"""

import asyncio
import json
from mcp_server import mcp

async def demonstrate_usage():
    """Demonstrate typical usage scenarios"""
    
    print("🧮 MCP Math Server - Spanish Math Assistant for VS Code Copilot")
    print("=" * 65)
    
    print("\n📋 Available Tools:")
    tools = await mcp.list_tools()
    for tool in tools:
        print(f"  🔧 {tool.name}")
        print(f"     {tool.description.split('.')[0]}.")
    
    print("\n🧪 Example Interactions (as Copilot would use them):")
    
    scenarios = [
        ("User asks: '¿Cuánto es 15 + 25?'", "calcular_matematicas", {"expresion": "15+25"}),
        ("User asks: 'What is 7 times 8?'", "calculate_math", {"expression": "7*8"}),
        ("User asks: 'Calculate (100-25)/3'", "calculate_math", {"expression": "(100-25)/3"}),
        ("User asks: '¿Qué es 10 dividido por 0?'", "calcular_matematicas", {"expresion": "10/0"}),
        ("Complex math", "calculate_math", {"expression": "((15+5)*2-10)/4"}),
    ]
    
    for i, (scenario, tool_name, args) in enumerate(scenarios, 1):
        print(f"\n{i}. {scenario}")
        print(f"   → Copilot calls: {tool_name}({args})")
        
        try:
            result = await mcp.call_tool(tool_name, args)
            # Extract the text content from the result
            if result and len(result) > 0 and len(result[0]) > 0:
                response_text = result[0][0].text
                print(f"   ✅ Server responds: '{response_text}'")
            else:
                print(f"   ⚠️  Unexpected result format: {result}")
        except Exception as e:
            print(f"   ❌ Error: {e}")
    
    print(f"\n🎯 Summary:")
    print(f"   • The MCP server provides math calculation tools")
    print(f"   • All responses are in Spanish (as requested)")
    print(f"   • VS Code Copilot can use these tools to answer math questions")
    print(f"   • The server handles errors gracefully in Spanish")
    print(f"   • Both Spanish and English tool interfaces are available")
    
    print(f"\n🚀 Ready for VS Code integration!")
    print(f"   Run: python mcp_server.py")

if __name__ == "__main__":
    asyncio.run(demonstrate_usage())
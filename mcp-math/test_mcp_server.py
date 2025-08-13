#!/usr/bin/env python3
"""
Test script for the MCP Math Server
"""

import asyncio
import json
from mcp_server import mcp

async def test_mcp_server():
    """Test the MCP server functionality"""
    print("Testing MCP Math Server")
    print("=" * 40)
    
    # Test listing tools
    print("\n1. Available Tools:")
    tools = await mcp.list_tools()
    for tool in tools:
        print(f"  - {tool.name}: {tool.description}")
    
    # Test calling tools
    print("\n2. Testing calcular_matematicas tool:")
    try:
        result = await mcp.call_tool('calcular_matematicas', {'expresion': '2+2'})
        print(f"  Input: '2+2' -> Output: {result}")
        
        result = await mcp.call_tool('calcular_matematicas', {'expresion': '(10-5)*3+1'})
        print(f"  Input: '(10-5)*3+1' -> Output: {result}")
        
        result = await mcp.call_tool('calcular_matematicas', {'expresion': '5/0'})
        print(f"  Input: '5/0' -> Output: {result}")
    except Exception as e:
        print(f"  Error: {e}")
    
    print("\n3. Testing calculate_math tool:")
    try:
        result = await mcp.call_tool('calculate_math', {'expression': '7*8'})
        print(f"  Input: '7*8' -> Output: {result}")
    except Exception as e:
        print(f"  Error: {e}")
    
    print("\n4. MCP Server is ready for VS Code integration!")

if __name__ == "__main__":
    asyncio.run(test_mcp_server())
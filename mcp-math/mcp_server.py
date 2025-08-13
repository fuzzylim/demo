#!/usr/bin/env python3
"""
MCP Math Agent Server - Provides math calculation tools in Spanish for VS Code Copilot
"""

import re
import sys
from mcp.server import FastMCP
from typing import Any, Dict

# Initialize the MCP server
mcp = FastMCP(
    name="math-spanish-server",
    instructions="Un servidor que resuelve operaciones matemáticas y responde en español."
)

def solve_math_expression(expression: str) -> str:
    """
    Safely evaluate a mathematical expression and return the result in Spanish.
    
    Args:
        expression: A mathematical expression containing numbers and basic operators
        
    Returns:
        The result in Spanish, or an error message
    """
    try:
        # Only allow numbers and basic operators for safety
        # Explicitly exclude ** (power operator) and other potentially dangerous operations
        if not re.match(r'^[0-9+\-*/(). ]+$', expression) or '**' in expression:
            return "Expresión no válida. Solo se permiten números y operadores básicos (+, -, *, /, paréntesis)."
        
        # Evaluate the expression safely
        result = eval(expression, {"__builtins__": None}, {})
        return f"La respuesta es: {result}"
    except ZeroDivisionError:
        return "Error: División por cero no está permitida."
    except SyntaxError:
        return "Error: La expresión matemática tiene errores de sintaxis."
    except Exception as e:
        return f"No pude calcular la respuesta: {str(e)}"

@mcp.tool()
def calcular_matematicas(expresion: str) -> str:
    """
    Calcula operaciones matemáticas básicas y devuelve el resultado en español.
    
    Soporta:
    - Suma (+)
    - Resta (-)
    - Multiplicación (*)
    - División (/)
    - Paréntesis para agrupar operaciones
    - Números enteros y decimales
    
    Args:
        expresion: La expresión matemática a calcular (ej: "2+2", "5*3+1", "(10-5)/2")
    """
    return solve_math_expression(expresion)

@mcp.tool()
def calculate_math(expression: str) -> str:
    """
    Calculate basic mathematical operations and return the result in Spanish.
    
    Supports:
    - Addition (+)
    - Subtraction (-)
    - Multiplication (*)
    - Division (/)
    - Parentheses for grouping operations
    - Integer and decimal numbers
    
    Args:
        expression: The mathematical expression to calculate (e.g., "2+2", "5*3+1", "(10-5)/2")
    """
    return solve_math_expression(expression)

if __name__ == "__main__":
    # Run the MCP server using stdio transport for VS Code integration
    mcp.run("stdio")
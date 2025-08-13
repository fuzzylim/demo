import re

def solve_math_expression(expression):
    try:
        # Only allow numbers and basic operators for safety
        if not re.match(r'^[0-9+\-*/(). ]+$', expression):
            return "Expresión no válida."
        result = eval(expression, {"__builtins__": None}, {})
        return f"La respuesta es: {result}"
    except Exception:
        return "No pude calcular la respuesta."

def handle_request(request):
    question = request.get("question", "")
    return {"answer": solve_math_expression(question)}

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/mcp", methods=["POST"])
def mcp_endpoint():
    data = request.get_json(force=True)
    response = handle_request(data)
    return jsonify(response)

if __name__ == "__main__":
    # Run as HTTP MCP server
    app.run(host="0.0.0.0", port=8080)

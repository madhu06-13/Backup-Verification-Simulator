import json

def format_ai_output(data: dict):
    """
    Formats final AI JSON output for UI or display
    """
    return {
        "ai_report": {
            "problem": data.get("problem", ""),
            "cause": data.get("cause", ""),
            "solution": data.get("solution", "")
        },
        "status": "generated"
    }
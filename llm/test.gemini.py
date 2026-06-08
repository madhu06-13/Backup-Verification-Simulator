from llm_engine import generate_explanation
import json

sample_data = {
    "status": "FAIL",
    "missing_rows": 10,
    "duplicates": 5,
    "schema_mismatch": True
}

result = generate_explanation(sample_data)

print("\n========== RAW JSON OUTPUT ==========\n")
print(json.dumps(result, indent=2))

print("\n========== FORMATTED VIEW ==========\n")

print("PROBLEM:\n", result["problem"])
print("\nCAUSE:\n", result["cause"])
print("\nSOLUTION:\n", result["solution"])
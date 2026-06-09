import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def get_ai_explanation(validation_result):

    try:

        prompt = f"""
        You are a backup verification expert.

        Issues found:
        {validation_result}

        Explain:
        - What went wrong
        - Why it happened
        - How to fix it
        """

        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt
        )

        return response.text

    except Exception:

        missing_rows = validation_result.get(
            "missing_rows", 0
        )

        duplicates = validation_result.get(
            "duplicates", 0
        )

        schema_issue = validation_result.get(
            "schema_mismatch", False
        )

        checksum_issue = not validation_result.get(
            "checksum_match", True
        )

        cause_list = []

        if missing_rows > 0:
            cause_list.append(
                f"{missing_rows} missing rows"
            )

        if duplicates > 0:
            cause_list.append(
                f"{duplicates} duplicate rows"
            )

        if schema_issue:
            cause_list.append(
                "schema mismatch detected"
            )

        if checksum_issue:
            cause_list.append(
                "checksum validation failed"
            )

        return f"""
Problem:
Backup verification failed.

Cause:
{', '.join(cause_list)}

Solution:
1. Re-run the backup process.
2. Verify data transfer integrity.
3. Check backup job logs.
4. Validate backup before deployment.
"""
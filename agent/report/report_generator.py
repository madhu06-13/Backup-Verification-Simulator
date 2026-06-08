import os
from agent.report.templates import SUCCESS_TEMPLATE, FAIL_TEMPLATE


def generate_report(validation_result, ai_result):

    # ✅ SAFE: ensure validation_result is dictionary
    if isinstance(validation_result, dict):
        status = validation_result.get("status")
    else:
        status = "FAIL"  # fallback if something went wrong

    # ✅ PASS case
    if status == "PASS":

        report = SUCCESS_TEMPLATE

    # ✅ FAIL case
    else:

        report = FAIL_TEMPLATE.format(
            problem=str(ai_result) if ai_result else "AI explanation not available",
            cause="Refer AI explanation above",
            solution="Refer AI explanation above"
        )

    # ✅ Ensure reports folder exists
    os.makedirs("reports", exist_ok=True)

    # ✅ Save report
    with open("reports/latest_report.md", "w", encoding="utf-8") as file:
        file.write(report)

    return report
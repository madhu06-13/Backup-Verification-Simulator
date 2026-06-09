import os
from agent.report.templates import SUCCESS_TEMPLATE, FAIL_TEMPLATE


def generate_report(validation_result, ai_result):

    
    if isinstance(validation_result, dict):
        status = validation_result.get("status")
    else:
        status = "FAIL"  # fallback if something went wrong

    if status == "PASS":

        report = SUCCESS_TEMPLATE

    else:

        report = FAIL_TEMPLATE.format(
            problem=str(ai_result) if ai_result else "AI explanation not available",
            cause="Refer AI explanation above",
            solution="Refer AI explanation above"
        )

   
    os.makedirs("reports", exist_ok=True)

    
    with open("reports/latest_report.md", "w", encoding="utf-8") as file:
        file.write(report)

    return report
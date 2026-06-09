from agent.workflow.execution_flow import execute
from agent.report.report_generator import generate_report


def run_agent(original_file, backup_file):

    result = execute(original_file, backup_file)

    validation = result.get("validation")
    ai_result = result.get("ai_analysis")

    
    if not isinstance(validation, dict):
        validation = {"status": "FAIL"}

    
    if ai_result is None:
        ai_result = "AI explanation not available"
    else:
        ai_result = str(ai_result)

    report = generate_report(validation, ai_result)

    return {
        "validation": validation,
        "ai_analysis": ai_result,
        "report": report
    }
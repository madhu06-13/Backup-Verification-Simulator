from validator.validator import validate
from agent.workflow.decision_engine import decide
from llm.llm_engine import get_ai_explanation


def execute(
    original_file,
    backup_file
):

    validation_result = validate(
        original_file,
        backup_file
    )

    action = decide(
        validation_result
    )

    ai_result = None

    if action == "CALL_AI":

        try:

            ai_result = get_ai_explanation(
                validation_result
            )

        except Exception:

            ai_result = {
                "problem": "Backup verification failed",
                "cause": (
                    f"{validation_result['missing_rows']} missing rows, "
                    f"{validation_result['duplicates']} duplicate rows detected."
                ),
                "solution": (
                    "Re-run the backup process and verify "
                    "data integrity before deployment."
                )
            }

    return {

        "validation": validation_result,

        "ai_analysis": ai_result

    }
def decide(validation_result):

    if validation_result["status"] == "FAIL":
        return "CALL_AI"

    return "SUCCESS"
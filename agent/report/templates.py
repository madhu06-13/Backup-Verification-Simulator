print(" TEMPLATES FILE LOADED")

SUCCESS_TEMPLATE = """
==========================
BACKUP VERIFICATION REPORT
==========================

STATUS : PASS

All validation checks passed successfully.

Backup is safe to use.
"""

FAIL_TEMPLATE = """
==========================
BACKUP VERIFICATION REPORT
==========================

STATUS : FAIL

AI ANALYSIS:
{problem}

CAUSE:
{cause}

SOLUTION:
{solution}
"""
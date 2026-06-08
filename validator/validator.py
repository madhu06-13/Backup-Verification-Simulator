from validator.checks.row_check import row_count_check
from validator.checks.missing_check import missing_row_check
from validator.checks.duplicate_check import duplicate_check
from validator.checks.schema_check import schema_check

from validator.hash.checksum import calculate_checksum


def validate(original_file, backup_file):

    row_result = row_count_check(
        original_file,
        backup_file
    )

    missing_rows = missing_row_check(
        original_file,
        backup_file
    )

    duplicates = duplicate_check(
        backup_file
    )

    schema_match = schema_check(
        original_file,
        backup_file
    )

    original_hash = calculate_checksum(
        original_file
    )

    backup_hash = calculate_checksum(
        backup_file
    )

    checksum_match = (
        original_hash == backup_hash
    )

    status = "PASS"

    if (
        missing_rows > 0
        or duplicates > 0
        or not schema_match
        or not checksum_match
    ):
        status = "FAIL"

    return {

        "status": status,

        "original_rows":
            row_result["original_rows"],

        "backup_rows":
            row_result["backup_rows"],

        "missing_rows":
            missing_rows,

        "duplicates":
            duplicates,

        "schema_mismatch":
            not schema_match,

        "checksum_match":
            checksum_match
    }
from validator.validator import validate


result = validate(

    "validator/test_data/original.csv",

    "validator/test_data/backup_bad.csv"

)

print(result)
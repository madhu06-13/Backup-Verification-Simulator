from agent.agent import run_agent


result = run_agent(

    "validator/test_data/original.csv",

    "validator/test_data/backup_bad.csv"

)

print("\n========== FINAL OUTPUT ==========\n")

print(result)

print("\n========== REPORT ==========\n")

print(result["report"])
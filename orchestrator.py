def ask_to_run_spark_jobs():
    answer = input("Do you want to run the jobs? (yes/no): ")
    if answer.lower() == "yes":
        return True
    else:
        return False
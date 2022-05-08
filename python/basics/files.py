from os.path import exists, getsize
from datetime import datetime

def main():
    """Provide possible ways to use this script.

    Does not handle user input errors.
    """
    update_log()

    action = int(input("Press 1 to view the log and 2 to clear it: "))

    if action == 1:
        get_log()
    else:
        clear_log()


def update_log():
    """Add the current execution time to the log file."""
    with open("executions.log", 'a') as log:
        current_time = str(datetime.now())
        log.write(current_time + "\n")


def get_log():
    """Read all execution times of this script from log the file."""
    if exists("executions.log") and getsize("executions.log") > 0:
        log = open("executions.log")

        for execution_time in log:
            print(f"Executed in {execution_time}", end="")

        log.close()
    else:
        file_name = __file__.split('/')[-1]
        print(f"{file_name} hasn't yet been executed...")


def clear_log():
    """Just clean the file log."""
    open("executions.log", 'w').close()
    print("Log has just been cleared.")


if __name__ == "__main__":
    main()


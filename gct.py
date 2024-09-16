import argparse
import random
from datetime import datetime, timedelta
import subprocess

def get_random_time():
    # Define start and end times
    start_time = datetime.strptime("08:00:00", "%H:%M:%S")
    end_time = datetime.strptime("23:00:00", "%H:%M:%S")
    
    # Calculate a random time between start_time and end_time
    delta = end_time - start_time
    random_seconds = random.randint(0, int(delta.total_seconds()))
    random_time = start_time + timedelta(seconds=random_seconds)
    
    return random_time.strftime("%H:%M:%S")

def gct(timezone, date, msg):
    time = get_random_time()
    
    # Define timezone suffixes
    timezone_suffix = {
        "ae": "+0400",
        "sl": "+0530"
    }.get(timezone)

    if not timezone_suffix:
        print("Invalid timezone. Use 'ae' or 'sl'.")
        return

    # Create the git commit command
    command = f"git commit --date='{date} {time} {timezone_suffix}' -m \"{msg}\""
    
    # Print and execute the command
    print("Executing command:")
    print(command)
    subprocess.run(command, shell=True)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a git commit with a random time and timezone.")
    parser.add_argument("timezone", choices=["ae", "sl"], help="Timezone: 'ae' or 'sl'")
    parser.add_argument("date", help="Date for the commit (format: YYYY-MM-DD)")
    parser.add_argument("msg", help="Commit message")

    args = parser.parse_args()
    
    gct(args.timezone, args.date, args.msg)

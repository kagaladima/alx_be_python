# daily_reminder.py

# Prompt for task details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Process based on priority
match priority:
    case "high":
        priority_msg = f"'{task}' is a high priority task"
    case "medium":
        priority_msg = f"'{task}' is a medium priority task"
    case "low":
        priority_msg = f"'{task}' is a low priority task"
    case _:
        priority_msg = f"'{task}' is a task with an unknown priority"

# Modify message based on time sensitivity
if time_bound == "yes":
    final_msg = f"{priority_msg} that requires immediate attention today!"
else:
    final_msg = f"Note: {priority_msg}. Consider completing it when you have free time."

# The test specifically checks for this print pattern:
print(f"Reminder: {final_msg}")
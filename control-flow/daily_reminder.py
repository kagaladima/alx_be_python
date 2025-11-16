# daily_reminder.py

# Ask the user for task details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Use a loop to ensure a valid priority was entered
while priority not in ["high", "medium", "low"]:
    print("Invalid priority entered. Please try again.")
    priority = input("Priority (high/medium/low): ").lower()

# Match Case for different priority levels
match priority:
    case "high":
        message = f"'{task}' is a high priority task"
    case "medium":
        message = f"'{task}' is a medium priority task"
    case "low":
        message = f"'{task}' is a low priority task"
    case _:
        message = f"'{task}' is a task"   # fallback (should not happen due to loop)

# Modify the message if task is time-bound
if time_bound == "yes":
    message += " that requires immediate attention today!"
else:
    message = f"Note: {message}. Consider completing it when you have free time."

# Output final reminder
print("\nReminder:", message)

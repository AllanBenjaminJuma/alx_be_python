task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

match priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
        elif time_bound == "no":
            print(f"Reminder: '{task}' is a high priority task. Try to complete it as soon as possible.")
        else:
            print("Invalid input for time sensitivity. Please enter 'yes' or 'no'.")

    case "medium":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a medium priority task that should be scheduled soon.")
        elif time_bound == "no":
            print(f"Reminder: '{task}' is a medium priority task. Add it to your plan for the week.")
        else:
            print("Invalid input for time sensitivity. Please enter 'yes' or 'no'.")

    case "low":
        if time_bound == "yes":
            print(f"Note: '{task}' is a low priority task but has a deadline. Don’t forget to complete it.")
        elif time_bound == "no":
            print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")
        else:
            print("Invalid input for time sensitivity. Please enter 'yes' or 'no'.")

    case _:
        print("Invalid priority entered. Please enter high, medium, or low.")

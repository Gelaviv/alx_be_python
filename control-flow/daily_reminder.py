task = input("Enter a task description:").lower()
priority = input("Enter priority level (high/medium/low):").lower()
time_bound = input("Is this task time bound? (yes/no)").lower()

match priority:
    case "high":
        if priority == "high" and time_bound == "yes":
            print(f"{task} is a high priority task and requires immediate attention today!")
        elif priority == "high" and time_bound == "no":
            print(f"{task} is a high priority task and needs to be completed within the week!")
    case "medium":
        if priority == "medium" and time_bound == "yes":
            print(f"{task} is a medium priority task that needs to be completed within the next two weeks!")
        elif priority == "medium" and time_bound == "no":
            print(f"{task} is a medium priority task that needs to be completed before next month!")
    case "low":
        if priority == "low" and time_bound == "yes":
            print(f"{task} is a low priority task. Ensure it is completed before the year runs out!")
        elif priority == "low" and time_bound == "no":
            print(f"{task} is a is a low priority task. Consider completing it when you have free time.") 
    case _:
        print("You have entered an invalid input")
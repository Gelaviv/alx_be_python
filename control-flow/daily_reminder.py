# task = input("Enter your task:").lower()
# priority = input("Enter priority level (high/medium/low):").lower()
# time_bound = input("Priority (high/medium/low):").lower()

# match priority:
#     case "high":
#         if time_bound == "yes":
#             print(f"{task} is a high priority task and requires immediate attention today!")
#         elif time_bound == "no":
#             print(f"{task} is a high priority task and needs to be completed within the week!")
#     case "medium":
#         if time_bound == "yes":
#             print(f"{task} is a medium priority task that needs to be completed within the next two weeks!")
#         elif time_bound == "no":
#             print(f"{task} is a medium priority task that needs to be completed before next month!")
#     case "low":
#         if time_bound == "yes":
#             print(f"{task} is a low priority task. Ensure it is completed before the year runs out!")
#         elif time_bound == "no":
#             print(f"{task} is a is a low priority task. Consider completing it when you have free time.") 
#     case _:
#         print("You have provided an invalid input")

task = input("Enter your task:").lower()
priority = input("Priority (high/medium/low):").lower()
time_bound = input("Is it time-bound? (yes/no):").lower()

match priority:
    case "high":
        if time_bound == "yes":
            print(f"{task} is a high priority task and requires immediate attention today!")
        else:
            print(f"{task} is a high priority task and needs to be completed within the week!")
    case "medium":
        if time_bound == "yes":
            print(f"{task} is a medium priority task that needs to be completed within the next two weeks!")
        else:
            print(f"{task} is a medium priority task that needs to be completed before next month!")
    case "low":
        if time_bound == "yes":
            print(f"{task} is a low priority task. Ensure it is completed before the year runs out!")
        else:
            print(f"{task} is a low priority task. Consider completing it when you have free time.") 
    case _:
        print("You have provided an invalid input")
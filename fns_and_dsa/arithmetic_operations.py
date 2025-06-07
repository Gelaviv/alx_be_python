def perform_operation(num1, num2, operation):
    match operation:
        case "add":
            addition = num1 + num2
            return addition
        case "subtract":
            subtraction = num1 - num2
            return subtraction

        case "multiply":
            multiplication = num1 * num2
            return multiplication
        case "divide":
            division = num1 / num2
            if num1 % num2 != 0:
                print("Numbers are not divisible by zero")
            else:
                return division
        case _:
            print("You have entered an invalid operation")
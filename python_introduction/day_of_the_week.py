def day_of_the_week(day):
    match day:
        case "Saturday" | "Sunday":
            print("It's a weekend!")
        case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
            print("It's a weekday!")
        case _:
            print("Not a day of the week!")
print(day_of_the_week("Sunday"))
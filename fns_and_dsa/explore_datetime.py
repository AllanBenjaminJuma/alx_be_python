from datetime import datetime, timedelta


def display_current_datetime():
    current_date = datetime.now()
    current_date_formatted = current_date.strftime("%Y-%m-%d %H:%M:%S")
    return current_date_formatted

def calculate_future_date(days):
    future_date = datetime.now() + timedelta(days)
    return future_date.strftime("%Y-%m-%d %H:%M:%S")

print(f"Today's date is: {display_current_datetime()}")

number_of_days = int(input("enter the number of days: "))
future_date = calculate_future_date(number_of_days)

print(f"The date after {number_of_days} days will be {future_date}")

    
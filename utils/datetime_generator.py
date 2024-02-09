from datetime import datetime, timedelta
import random

def random_datetime_in_range(start_date_str, end_date_str):
    # Convert the input date strings to datetime objects
    start_date = datetime.strptime(start_date_str, "%d/%m/%Y %H")
    end_date = datetime.strptime(end_date_str, "%d/%m/%Y %H")

    # Calculate the range duration
    delta = end_date - start_date

    # Generate a random timedelta within the range duration
    random_timedelta = random.uniform(0, delta.total_seconds())
    random_duration = timedelta(seconds=random_timedelta)

    # Calculate the random datetime within the range
    random_datetime = start_date + random_duration

    return random_datetime

# Example usage:
#start_date_str = "01/01/2023 00"
#end_date_str = "31/12/2023 23"
#random_date = random_datetime_in_range(start_date_str, end_date_str)

#print("Random DateTime:", random_date.strftime("%d/%m/%Y %H:%M:%S"))

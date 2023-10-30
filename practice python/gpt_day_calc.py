from datetime import datetime

def days_passed_in_year(date_input):
    # Get the current date
    current_date = datetime.now()
    
    # Convert the input string to a datetime object
    input_date = datetime.strptime(date_input, '%Y-%m-%d')
    
    # Check if the input date is in the past
    if input_date > current_date:
        return "Please enter a date in the past."

    # Get the days passed in the year
    days_passed = (current_date - input_date).days

    # Get the total days in the current year
    total_days_in_year = (datetime(current_date.year + 1, 1, 1) - datetime(current_date.year, 1, 1)).days

    return days_passed, total_days_in_year

# Input a date in the format 'YYYY-MM-DD'
date_input = input("Enter a date in the format 'YYYY-MM-DD': ")

result = days_passed_in_year(date_input)
if isinstance(result, tuple):
    days_passed, total_days = result
    print(f"Days passed in the year after {date_input}: {days_passed} out of {total_days} days.")
else:
    print(result)

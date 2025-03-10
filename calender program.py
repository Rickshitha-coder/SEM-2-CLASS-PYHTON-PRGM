print("Getting the first weekday and number of days in a month")
import calendar
year = 2024 #get the Input year and month 
month = 8 
first_weekday, num_days = calendar.monthrange(year, month) # Get the first weekday and the number of days in the month 
print(f"First weekday: {first_weekday}, Number of days: {num_days}")


print(" Iterating over the days of a month")
for day in calendar.Calendar().itermonthdays(year, month):    # Iterate over the days of the month
    print(day)

print("Example ….TO DISPLAY A CALENDAR")
# Create a TextCalendar instance 
text_cal = calendar.TextCalendar(calendar.SUNDAY)  # SUNDAY as the starting day of the week 
year = 2024 
month = 8 # Generate a plain-text calendar for a specific month 
plain_text_cal = text_cal.formatmonth(year, month) 
print(plain_text_cal)   # Print the plain-text calendar 


print("To display the past dates…")
from datetime import datetime, timedelta 
now = datetime.now() # Get the current date and time 
print(f"Current date and time: {now}") 
# Specify how many days/hours/minutes in the past you want to go 
days_in_past = 10
hours_in_past = 5 
minutes_in_past = 30 
# Subtract time using timedelta 
past_time = now - timedelta(days=days_in_past, hours=hours_in_past, minutes=minutes_in_past) 
print(f"Past date and time (5 days, 3 hours, 30 minutes ago): {past_time}") 


print("Example : Change the first letter to caps..")
# Example of capwords function
import string
sentence = "this is my day"  
capitalized_sentence = string.capwords(sentence)   #first word in caps in each words 
print(capitalized_sentence) 

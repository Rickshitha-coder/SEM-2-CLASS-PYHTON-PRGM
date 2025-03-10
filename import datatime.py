import datetime
current_datetime=datetime.datetime.now() #get the current date and time
print(current_datetime)
current_date=datetime.date.today()  #get the current date only
print(current_date)
specific_date=datetime.date(2023,9,23) #creating a specific date(year, month, day)
print(specific_date)
specific_time=datetime.time(14,30,45)  #creating a specific time(hour,mintue,second).
print(specific_time)
specific_datetime=datetime.datetime(2024,9,23,14,30,45) #creating a specific date and time(year,month ,day,hour,minute,second)
print(specific_datetime)
formatted_date=current_datetime.strftime("%Y-%m-%d %H:%M:%S")  #formatting date and time inot a string
print("Formatted date and time:",formatted_date)
date_string="2024-09-23 14:30:45"
parsed_date=datetime.datetime.strptime(date_string,"%Y-%m-%d %H:%M:%S") #parsing a date string into a datetime object
print("Parsed datetime object:",parsed_date)
ten_days=datetime.timedelta(days=10)  #create a timedelta of 10 days
print(ten_days)
date_10_days_ago=current_date-ten_days #subtract 10 days rom the current date
print("Date 10 days ago:",date_10_days_ago)
date_10_days_later=current_date+ten_days  #add 10 days o the current date
print("Date 10 Days later:",date_10_days_later)
date1=datetime.date(2024,10,8)
date2=datetime.date(2020,4,24)
difference=date1-date2
print("Difference between teo dates:",difference.days,"days")


import pytz
current_utc=datetime.datetime.now(pytz.utc)  #get the current in UTC
print("Current UTC time:",current_utc)
eastern=pytz.timezone('US/Eastern')  #convert UTC  time to a specific time zone
eastern_time=current_utc.astimezone(eastern)
print("Eastern time:",eastern_time)

# # from datetime import datetime
# # now = datetime.now()
# # print(now)                      # 2021-07-08 07:34:46.549883
# # day = now.day                   # 8
# # month = now.month               # 7
# # year = now.year                 # 2021
# # hour = now.hour                 # 7
# # minute = now.minute             # 38
# # second = now.second
# # timestamp = now.timestamp()
# # print(day, month, year, hour, minute)
# # print('timestamp', timestamp)
# # print(f'{day}/{month}/{year}, {hour}:{minute}')  # 8/7/2021, 7:38 

# from datetime import datetime
# now = datetime.now()
# # ISO-like format
# print(now.strftime("%Y-%m-%d %H:%M:%S"))
# # Custom readable format
# print(now.strftime("Today is %A, %B %d, %Y"))
# # 12-hour format with AM/PM
# print(now.strftime("%I:%M:%S %p"))

''' 
Get the current day, month, year, hour, minute and timestamp from datetime module
Format the current date using this format: "%m/%d/%Y, %H:%M:%S")
Today is 5 December, 2019. Change this time string to time.
Calculate the time difference between now and new year.
Calculate the time difference between 1 January 1970 and now.
Think, what can you use the datetime module for? Examples:
Time series analysis
To get a timestamp of any activities in an application
Adding posts on a blog
🎉 CONGRATULATIONS ! 🎉
''' 

from datetime import datetime 

now=datetime.now() 
print(now)

#ISO liked format 
print (now.strftime("%m/%d/%Y, %H:%M:%S")) 

date_string = "5 December, 2019"
print("date_string =", date_string)     # date_string = 5 December, 2019
date_object = datetime.strptime(date_string, "%d %B, %Y")
print("date_object =", date_object)     # date_object = 2019-12-05 00:00:00
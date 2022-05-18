# we often need current date and time when logging errors and saving data

# to get current date and time 
# we need to use the datetime library 
from datetime import datetime, timedelta

today = datetime.now()
# the now function returns a datatime object
print('today is: '+ str(today))

# timedelta is used to define a period of time 
one_day = timedelta(days=1)
yesterday = today - one_day
print('Yesterday was: '+ str(yesterday))

current_date = datetime.now()

print('Day: ' + str(current_date.day))
print('Month: ' + str(current_date.month))
print('Year: ' + str(current_date.year))

birthday = input('When is your birthday (dd/mm/yyyy)? ')

birthday_date = datetime.strptime(birthday, '%d/%m/%Y')

print('Birthday: '+ str(birthday_date))
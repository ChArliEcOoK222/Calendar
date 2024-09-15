# How do I list the events for today?
# How do I list the events for this week?
# How do I list the events for this month?
# How do I list the events for this year
# How do I add and delete things to my calendar?
# How do I put this into a bash script?
# How do I run this using Alfred?

### Required Libraries
from gcsa.google_calendar import GoogleCalendar 
from datetime import datetime
import datetime


### Variable to store the  email address in order to access the google calendar
calendar = GoogleCalendar('charlie2007.cook@gmail.com')

## Function to list all calendar events today
def list_events_today():
    # Assigning today's date to a variable
    date_tdy = datetime.datetime.today()
    # Assigning tomorrow's date to a variable
    date_tmrw = datetime.datetime.today() + datetime.timedelta(days=1)
    # Assigning the events for today into a variable
    events = calendar.get_events(date_tdy, date_tmrw, order_by='updated')
    # Converting the generator object to a string using list comprehension
    results = ''.join([str(x) for x in events])
    # Outputting the events to the terminal
    print(result)
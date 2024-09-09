# How do I list the calendar events?
# How do I add and delete things to my calendar?
# How do I put this into a bash script?
# How do I run this using Alfred?

### Required Libraries
from gcsa.google_calendar import GoogleCalendar 

## Function to list calendar events

# Variables to store the credentials and email address in order to access the google calendar
from gcsa.google_calendar import GoogleCalendar

calendar = GoogleCalendar('your_email@gmail.com')
for event in calendar:
    print(event)
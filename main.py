# How do I add and delete things to my calendar?
# How do I put this into a bash script?
# How do I run this using Alfred?

### Required Libraries
from gcsa.google_calendar import GoogleCalendar 

## Listing calendar events
gc = GoogleCalendar(credentials_path='/Users/charlie/Documents/Calendar/credentials.json')
calendar = GoogleCalendar('charlie2007.cook@gmail.com')

for event in calendar:
    print(event)
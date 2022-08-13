import pytz
from datetime import datetime

for i in sorted(pytz.country_names):
    try:
        print(f'Name {pytz.country_names[i]} Time Zone : {pytz.country_timezones[i]}')
    except:
        print(f'Country Time zone not found : {pytz.country_names[i]}')

for i in sorted(pytz.country_names):
    print(f'Name {pytz.country_names[i]} Time Zone : {pytz.country_timezones.get(i, "NA")}')

print(datetime.now(tz=pytz.timezone('Asia/Kolkata')))



